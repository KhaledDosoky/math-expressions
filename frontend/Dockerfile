# ------------------------------------------------------------------
# STAGE 1: Build the Next.js application (Build Environment)
# ------------------------------------------------------------------
# Use 'slim' for build compatibility and caching.
FROM node:20-slim as builder

# Set working directory for the build process
WORKDIR /app

# Copy and install dependencies (Leverage Docker caching)
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# IMPORTANT: Ensure 'output: "standalone"' is set in your next.config.js
ENV NEXT_TELEMETRY_DISABLED 1

# Build the application, creating the standalone directory
ENV NODE_OPTIONS="--max-old-space-size=512"
RUN npm run build

# ------------------------------------------------------------------
# STAGE 2: Create the absolute minimum final image (Production Runtime)
# ------------------------------------------------------------------
# Use the official Distroless Node.js image for maximum size reduction.
# The user in this image is typically 'nonroot' (UID 65532).
FROM gcr.io/distroless/nodejs20 as runner

# The non-root user (UID 65532) in Distroless Node.js images
ENV UID=65532
USER ${UID}

# Set the final working directory to the expected standalone location
# Distroless images often use a minimal user's home directory for permissions.
WORKDIR /app

# CRITICAL: Copy the contents of the standalone folder to the WORKDIR.
# The standalone folder contains the server.js and all required node_modules.
COPY --from=builder --chown=${UID}:${UID} /app/.next/standalone/ ./

# Copy public and static files which are NOT included in 'standalone'
COPY --from=builder --chown=${UID}:${UID} /app/public ./public
COPY --from=builder --chown=${UID}:${UID} /app/.next/static ./.next/static

# Expose the port (default 3000)
EXPOSE 3000

# Start the Next.js server.
# CRITICAL: Must use the 'exec form' (JSON array) and ensure the node binary is on the PATH.
# The Distroless Node.js image ensures 'node' is the default ENTRYPOINT or is on the PATH.
CMD ["server.js"]