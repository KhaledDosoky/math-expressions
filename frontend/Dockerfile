# 1. Install dependencies and build the app
FROM node:20-alpine AS builder

WORKDIR /app
COPY package.json .
COPY package-lock.json .

# Install production and development dependencies
RUN npm install

# Copy source code and build the application
COPY . .
RUN npm run build

# 2. Run the production app
FROM node:20-alpine AS runner

WORKDIR /app

# Set production environment (important for Next.js)
ENV NODE_ENV production

# Copy necessary files from the builder stage
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/public ./public

# Expose the port Next.js runs on
EXPOSE 3000

# Start the Next.js server
CMD ["npm", "start"]