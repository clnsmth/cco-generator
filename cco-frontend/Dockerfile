# Use Node 20 (LTS)
FROM node:20-alpine

WORKDIR /app

# 1. Install dependencies first (caching layer)
COPY package.json package-lock.json ./
RUN npm ci

# 2. Copy source code
COPY . .

# 3. Expose the port Vite uses
EXPOSE 3000

# 4. Start the dev server
# --host 0.0.0.0 is required to expose it outside the container
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
