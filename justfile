# Justfile for Math Expressions App
# Run `just --list` to see all available recipes

# Default recipe (runs when you just type `just`)
default: dev

# Development recipes
dev: dev-full

# Run both frontend and backend in development mode
dev-full:
    #!/usr/bin/env bash
    echo "Starting full-stack development environment..."
    echo "Frontend will be available at http://localhost:3000"
    echo "Backend will be available at http://localhost:8000"
    echo ""
    echo "Press Ctrl+C to stop both services"
    trap 'kill 0' INT
    (cd frontend && npm run dev) &
    (cd backend && uv run uvicorn single_server:app --host 0.0.0.0 --port 8000) &
    wait

# Run frontend in development mode
dev-frontend:
    cd frontend && npm run dev

# Run backend in development mode
dev-backend:
    cd backend && uv run uvicorn single_server:app --host 0.0.0.0 --port 8000

# Build recipes
build: build-full

# Full build (frontend + backend integration)
build-full:
    ./build.bash

# Build frontend only
build-frontend:
    cd frontend && npm run build

# Build backend (install dependencies)
build-backend:
    cd backend && uv sync

# Testing and quality recipes
lint:
    cd frontend && npm run lint

type-check:
    cd frontend && npx tsc --noEmit

# Install dependencies
install-deps: install-frontend install-backend

install-frontend:
    cd frontend && npm install

install-backend:
    cd backend && uv sync

# PWA utilities
convert-icons:
    cd frontend && node convert-icons.js

# Clean build artifacts
clean:
    rm -rf frontend/out
    rm -rf frontend/.next
    rm -rf backend/static_files/*
    rm -rf backend/__pycache__
    rm -rf frontend/node_modules/.cache

# Full clean (including dependencies)
clean-all: clean
    rm -rf frontend/node_modules
    rm -rf backend/.venv

# Setup the project from scratch
setup: install-deps convert-icons build-full

# Run the production server
serve:
    cd backend && uv run uvicorn single_server:app --host 0.0.0.0 --port 8000

# Development helpers
format:
    cd frontend && npx eslint --fix .

# Check everything is working
check: lint type-check build-frontend