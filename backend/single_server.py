import os
import asyncio
import json
import threading
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from sse_starlette import EventSourceResponse # Keeping this import as you chose it
from starlette.responses import FileResponse, PlainTextResponse
from starlette.middleware.cors import CORSMiddleware

from Interpreter import StreamingInterpreter

# NOTE: The 'StreamingResponse' import was not used and is removed for cleanliness.

# --- Configuration (Must match the paths set up by build.sh) ---
# This path points to the 'static_files' folder created by the build.sh script.
# In a single container, this folder should be placed next to main.py.
FRONTEND_DIST_DIR = os.path.join(os.path.dirname(__file__), "static_files")

app = FastAPI(
    title="NextJS/FastAPI Playground",
    description="Serves the static Next.js frontend and provides the /api endpoints."
)

# 1. CORS Middleware (Essential for development/local testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Endpoints ---

# Define your custom API routes here, e.g., for streaming code execution
@app.get("/api/health")
def health_check():
    """Simple health check for the backend service."""
    return {"status": "ok", "service": "fastapi"}

# --- SSE Implementation ---

# NOTE: The EventSourceResponse requires the generator to be inside the route 
# or passed as an argument, as you have done.

@app.get("/api/stream") # <<< FIX: Changed path from "/stream" to "/api/stream"
async def stream_expr(code: str = Query(...)):
    
    # --- Inner Event Generator Function ---
    async def event_generator():
        loop = asyncio.get_event_loop()
        queue = asyncio.Queue()

        def stream_callback(json_data: str):
            """
            Called by the interpreter with a JSON string representing a single event.
            The JSON structure is {'type': '...', 'content': '...'}.
            """
            # Pass the raw JSON string to the queue
            loop.call_soon_threadsafe(queue.put_nowait, json_data)

        def run_interpreter():
            # NOTE: Assuming StreamingInterpreter is imported and available.
            try:
                interpreter = StreamingInterpreter()
                interpreter.env = {}
                # Set the unified callback
                interpreter.set_stream_callback(stream_callback)

                # 1. Run the interpreter
                interpreter.interpret(code)
                
            except Exception as e:
                # 2. Catch unexpected, *non-interpreter* fatal errors (e.g., memory, system)
                error_message = f"FATAL SERVER ERROR: {type(e).__name__}: {str(e)}"
                
                # Stream the fatal error as a structured JSON object
                error_json = json.dumps({'type': 'fatal_error', 'content': error_message})
                loop.call_soon_threadsafe(queue.put_nowait, error_json)
                
            finally:
                # 3. Stream the final environment snapshot (send the raw dict)
                try:
                    # IMPORTANT: Send the raw dictionary object, not a formatted string
                    env_snapshot_dict = interpreter.env
                    final_env_json = json.dumps({
                        'type': 'env_snapshot', 
                        'content': env_snapshot_dict # Send the dictionary here
                    })
                except Exception:
                    final_env_json = json.dumps({
                        'type': 'fatal_error', 
                        'content': "Failed to serialize final environment."
                    })
                
                loop.call_soon_threadsafe(queue.put_nowait, final_env_json)
                # 4. Signal end of stream
                loop.call_soon_threadsafe(queue.put_nowait, None)

        # Run interpreter in a thread so it doesn't block the event loop
        threading.Thread(target=run_interpreter, daemon=True).start()

        # 5. Consume the queue and format as Server-Sent Events (SSE)
        while True:
            # The msg here is the raw JSON string (e.g., '{"type": "stdout", "content": "..."}')
            msg = await queue.get()
            
            if msg is None:
                break

            # Yield the message formatted as an SSE packet
            yield f"data: {msg}\n\n"

    # --- Return the EventSourceResponse ---
    # EventSourceResponse handles setting the media_type="text/event-stream" header
    return EventSourceResponse(event_generator())


# --- Frontend Serving Configuration ---

# 2. Serve the Core Next.js Static Assets
# Next.js requests most of its compiled JS/CSS files from the /_next/static path.
# This mount point maps the external URL /_next/static to the internal folder static_files/_next/static.
app.mount(
    "/_next/static",
    StaticFiles(directory=os.path.join(FRONTEND_DIST_DIR, "_next/static")),
    name="nextjs_static_assets"
)

# NOTE: The previous app.mount("/", StaticFiles(...)) for root-level files 
# has been removed because it conflicts with client-side routing (SPA behavior).
# Root-level assets are now handled in the catch-all below.

# 3. Catch-all for Frontend HTML Pages
# This must be the *LAST* route defined to handle all requests not covered by API or specific static mounts.
@app.get("/{full_path:path}")
async def serve_nextjs_frontend(full_path: str):
    """
    Serves the main index.html for all non-API and non-static asset routes. 
    This is necessary for client-side routing (deep linking) to work.
    """
    
    # 1. Check if the requested path is a specific root-level static file 
    # (like favicon.ico or a manifest file). We serve it directly if found.
    static_asset_path = os.path.join(FRONTEND_DIST_DIR, full_path)
    if os.path.exists(static_asset_path) and not os.path.isdir(static_asset_path):
        return FileResponse(static_asset_path)

    # 2. Try to serve the requested path as an HTML file (e.g., /about -> /about.html)
    # This handles deep-linking to static pages that Next.js may have generated.
    file_path = os.path.join(FRONTEND_DIST_DIR, f"{full_path}.html")
    
    if os.path.exists(file_path):
        return FileResponse(file_path)

    # 3. For the root path, or any path that doesn't resolve to a static HTML file, 
    # serve the main index.html file. The client-side router will take over.
    index_file_path = os.path.join(FRONTEND_DIST_DIR, "index.html")
    
    if os.path.exists(index_file_path):
        return FileResponse(index_file_path)
    
    # Final fallback if the build directory is completely empty
    return PlainTextResponse(
        f"Server configured, but index.html not found. Checked path: {index_file_path}", 
        status_code=404
    )
