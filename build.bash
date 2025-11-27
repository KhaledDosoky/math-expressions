#!/bin/bash

# --- Configuration ---
FRONTEND_DIR="frontend"
BACKEND_DIR="backend"
FRONTEND_BUILD_OUTPUT="out" # Next.js static export target directory
BACKEND_STATIC_TARGET="static_files" # Directory FastAPI serves from
# ---------------------

echo "--- Starting Full-Stack Build Process ---"

# --- 1. Frontend Build (Next.js Static Export) ---
echo "1. Building Next.js Frontend (Static Export)..."
cd $FRONTEND_DIR || { echo "Error: Frontend directory not found."; exit 1; }

# Install dependencies if node_modules is missing
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

# Run the Next.js build command (creates the 'out/' folder)
npm run build || { echo "Error: Next.js build failed."; exit 1; }

echo "Frontend build completed in $FRONTEND_DIR/$FRONTEND_BUILD_OUTPUT/"

# Go back to the root directory
cd ..

# --- 2. Clean and Copy Artifacts to Backend ---
echo "2. Preparing Backend Static Files..."

TARGET_PATH="$BACKEND_DIR/$BACKEND_STATIC_TARGET"
SOURCE_CONTENTS="$FRONTEND_DIR/$FRONTEND_BUILD_OUTPUT/*"

echo "  > Target Path (Cleanup): $TARGET_PATH"
echo "  > Source Path (Copy):    $FRONTEND_DIR/$FRONTEND_BUILD_OUTPUT"

# Ensure the backend static target directory exists
mkdir -p "$TARGET_PATH"

# Remove old contents from the backend target directory
echo "  > Removing old artifacts from $TARGET_PATH..."
rm -rf "$TARGET_PATH"/*

# Copy the new static files from the Next.js 'out' directory
# CRITICAL: We copy the CONTENTS of the 'out' folder, not the 'out' folder itself.
echo "  > Copying contents of $FRONTEND_DIR/$FRONTEND_BUILD_OUTPUT to $TARGET_PATH..."
cp -R "$FRONTEND_DIR/$FRONTEND_BUILD_OUTPUT/." "$TARGET_PATH" || { echo "Error: Copy command failed."; exit 1; }

# --- 3. Verification ---
echo "3. Verifying Copy Operation..."

VERIFY_FILE="$TARGET_PATH/index.html"

if [ -f "$VERIFY_FILE" ]; then
    echo "SUCCESS: index.html found at $VERIFY_FILE. Frontend is ready."
else
    # This block executes if the copy failed. We report the exact path checked.
    echo "ERROR: index.html NOT FOUND at expected path:"
    echo "       $VERIFY_FILE"
    echo "       Please ensure your 'out' directory contains 'index.html'."
    exit 1
fi

# --- 4. Finalizing Backend Setup (Python) ---
echo "4. Installing Python Dependencies..."
# This step is typically needed before containerizing the backend
echo "--- Build Complete! ---"
echo "You can now run your FastAPI server."
cd $BACKEND_DIR || { echo "Error: Backend directory not found."; exit 1; }
uv run uvicorn single_server:app --host 0.0.0.0 --port 8000
