# Dockerfile.backend

# -----------------------------------------------------
# --- Stage 1: Builder Stage 🏗️ ---
# -----------------------------------------------------
FROM python:3.11-slim as builder

# Set environment variables
ENV APP_HOME=/backend
WORKDIR $APP_HOME

# Install uv globally first
RUN pip install --upgrade uv

# 1. Copy project files for dependency resolution
COPY pyproject.toml .
COPY uv.lock .

# 2. Install dependencies into a non-activated venv
# The .venv directory now holds ONLY the site-packages, not a primary interpreter.
RUN uv venv
RUN uv pip install .

# -----------------------------------------------------
# --- Stage 2: Runtime Stage 🚀 (The FINAL, WORKING SOLUTION) ---
# -----------------------------------------------------
FROM gcr.io/distroless/python3-debian12:nonroot

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/backend
WORKDIR $APP_HOME

# 1. Copy the virtual environment (specifically the site-packages) from the builder stage
# We only need the installed packages and associated metadata.
COPY --from=builder $APP_HOME/.venv $APP_HOME/.venv

# 2. Copy the application code
COPY *.py .
COPY Expr* .

# 3. CRITICAL: Add the virtual environment's site-packages to the Python path
# This tells the native Distroless Python interpreter where to find your installed packages (uvicorn).
ENV PYTHONPATH="$APP_HOME/.venv/lib/python3.11/site-packages"

# The Distroless image's built-in Python is at /usr/bin/python3.11 (or similar).
# We use the generic 'python3' that Distroless provides via its ENTRYPOINT.
ENTRYPOINT [ "/usr/bin/python3" ]

# Command to run the Python server
# We rely on the implicit ENTRYPOINT and execute the uvicorn module.
CMD ["-m", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]