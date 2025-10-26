# Dockerfile.backend

# Use a Python base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/backend
WORKDIR $APP_HOME

# Install uv globally first
RUN pip install --upgrade uv

# 1. Copy pyproject.toml and uv.lock from the subdirectory into the container's WORKDIR (for dependency resolution)
# Source path is relative to the root context: backend/
# Destination path is the current WORKDIR: .
COPY pyproject.toml .
COPY uv.lock .

# 2. Install dependencies (uv reads pyproject.toml from the current directory)
RUN uv venv
RUN uv pip install .

# 3. Copy the rest of the application code (server.py, etc.)
# Copy the *contents* of the backend subdirectory into the WORKDIR.
COPY . .

# Command to run the Python server (uses the robust module-execution method)
CMD ["uv", "run", "python", "-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]