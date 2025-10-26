# 1. Install dependencies and build the app
FROM node:20-alpine AS builder

WORKDIR /frontend
COPY package.json .
COPY package-lock.json .

# Install production and development dependencies
RUN npm install

# Copy source code and build the application
COPY . .
RUN npm run build

# 2. Run the production app
FROM node:20-alpine AS runner

WORKDIR /frontend

# Set production environment (important for Next.js)
ENV NODE_ENV development

# Copy necessary files from the builder stage
COPY --from=builder /frontend/.next ./.next
COPY --from=builder /frontend/node_modules ./node_modules
COPY --from=builder /frontend/package.json ./package.json
COPY --from=builder /frontend/public ./public

# Expose the port Next.js runs on
EXPOSE 3000

# Start the Next.js server
CMD ["npm", "start"]