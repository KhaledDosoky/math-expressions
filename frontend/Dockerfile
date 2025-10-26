# ------------------------------------------------------------------
# STAGE 1: Build the Next.js application (Build Environment)
# ------------------------------------------------------------------
FROM node:20-slim as builder

# Set working directory for the build process
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock/pnpm-lock.yaml)
# to install dependencies
COPY package.json package-lock.json ./

# Install dependencies, caching them if possible
RUN npm install

# Copy the rest of the application code
COPY . .

# Enable standalone mode for minimal size and no dependencies on node_modules at runtime
# NOTE: Ensure 'output: "standalone"' is set in your next.config.js
ENV NEXT_TELEMETRY_DISABLED 1

# Build the application
# This command generates the optimized build and the standalone folder
RUN npm run build

# ------------------------------------------------------------------
# STAGE 2: Create the minimal final image (Production Runtime)
# ------------------------------------------------------------------
# Use the official Next.js recommendation: a minimal Linux base image.
# node:20-slim is good, but often distroless or alpine are smaller.
# Alpine is a good compromise for size and available tools.
FROM node:20-alpine as runner

# Set the user to 'nextjs' for security best practices
# Next.js standalone mode is built to run as a non-root user.
RUN addgroup -g 1001 -S nextjs && adduser -u 1001 -S nextjs -G nextjs

# Set working directory in the final image
WORKDIR /app

# Copy the standalone folder from the builder stage.
# The 'standalone' folder contains *only* the necessary files (no node_modules).
COPY --from=builder --chown=nextjs:nextjs /app/.next/standalone ./

# Copy static files and public folder
COPY --from=builder --chown=nextjs:nextjs /app/public ./public
COPY --from=builder --chown=nextjs:nextjs /app/.next/static ./.next/static

# Expose the port the Next.js server will run on (default 3000)
EXPOSE 3000

# Switch to the non-root user
USER nextjs

# Start the Next.js server
CMD ["node", "server.js"]