# Stage 1: Build
FROM node:20-alpine AS builder

WORKDIR /frontend
COPY package.json package-lock.json ./

# Install all dependencies (including dev for build)
RUN npm ci

COPY . .

# Build the Next.js app
RUN npm run build

# Stage 2: Production runtime
FROM node:20-alpine AS runner

WORKDIR /frontend
ENV NODE_ENV=production

# Copy only production dependencies
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

# Copy built files and public assets
COPY --from=builder /frontend/.next ./.next
COPY --from=builder /frontend/public ./public

EXPOSE 3000
CMD ["npm", "start"]
