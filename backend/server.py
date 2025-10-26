import asyncio
import json
import threading
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette import EventSourceResponse
from Interpreter import StreamingInterpreter  # <-- your interpreter class

app = FastAPI()

# CORS setup (adjust for production)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stream")
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
            interpreter = StreamingInterpreter()
            interpreter.env = {}
            # Set the unified callback
            interpreter.set_stream_callback(stream_callback)

            try:
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
                        'content': env_snapshot_dict  # Send the dictionary here
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
    return EventSourceResponse(event_generator())