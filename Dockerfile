# This Dockerfile should be placed in the project's root directory.
# It uses a three-stage process:
# 1. frontend_builder: Compiles the Next.js static output (to 'out').
# 2. python_builder: Installs all Python dependencies using 'uv'.
# 3. runtime: Creates the final, minimal image by combining the compiled frontend
#             and the installed Python packages from the previous stages.

# -----------------------------------------------------
# --- Stage 0: Frontend Builder (Next.js Static Export) ⚛️ ---
# -----------------------------------------------------
FROM node:20-alpine AS frontend_builder
ENV APP_HOME=/app
WORKDIR $APP_HOME

# Copy only necessary files for dependency resolution
COPY frontend/package*.json ./

# Install frontend dependencies
RUN npm install

# Copy all source files
COPY frontend/ .

# Run the static build command. This creates the 'out/' directory.
# The `output: 'export'` flag MUST be set in frontend/next.config.js for this to work.
RUN npm run build

# -----------------------------------------------------
# --- Stage 1: Python Builder (Dependency Installation via uv) 🐍 ---
# -----------------------------------------------------
FROM python:3.11-slim AS python_builder

ENV APP_HOME=/backend
WORKDIR $APP_HOME

# Install uv globally first
RUN pip install --upgrade uv

# Copy only the files needed for uv installation
# Assuming pyproject.toml and uv.lock are in the /backend folder
COPY backend/pyproject.toml .
COPY backend/uv.lock .

# Install dependencies into a non-activated venv
RUN uv venv
# Run uv pip install . (assuming this command installs your main dependencies)
RUN uv pip install .

# -----------------------------------------------------
# --- Stage 2: Runtime Stage (Final Image) 🚀 ---
# -----------------------------------------------------
# Uses a secure, minimal Distroless image with Python 3.11
FROM gcr.io/distroless/python3-debian12:nonroot

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/backend
WORKDIR $APP_HOME

# 1. Copy the virtual environment (specifically the site-packages) from the builder stage
# We only need the installed packages.
COPY --from=python_builder $APP_HOME/.venv $APP_HOME/.venv

# 2. Copy the Python application code
# Assuming your main FastAPI file is 'main.py' based on the standard name, 
# though the user's CMD suggests 'server:app'. We'll copy main.py and use it in the CMD.
COPY backend/*.py .
COPY backend/Expr* .

# 3. CRITICAL: Copy the compiled Next.js static assets
# This copies the contents of the 'out/' folder from the frontend builder stage
# into the 'static_files' directory that main.py is configured to serve.
# The COPY command will automatically create the /backend/static_files directory.
# RUN mkdir -p $APP_HOME/static_files  <<< REMOVED THIS LINE
COPY --from=frontend_builder /app/out $APP_HOME/static_files

# 4. CRITICAL: Add the virtual environment's site-packages to the Python path
ENV PYTHONPATH="$APP_HOME/.venv/lib/python3.11/site-packages"

# Set the entrypoint for the Distroless image
ENTRYPOINT [ "/usr/bin/python3" ]

EXPOSE 8000

# Command to run the Python server
# NOTE: Adjusted CMD to use 'main:app' assuming your FastAPI file is 'main.py'
# If your FastAPI application object is named 'server:app', change this line.
CMD ["-m", "uvicorn", "single_server:app", "--host", "0.0.0.0", "--port", "8000"]
