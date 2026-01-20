/// <reference types="vitest" />
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
  server: {
    host: true, // Needed for Docker mapping
    port: 3000, 
    watch: {
      usePolling: true // often needed for Docker on Windows/Mac
    },
    proxy: {
      // Route all requests starting with /api to the FastAPI backend
      '/api': {
        target: 'http://backend:8000', // Matches the docker-compose service name
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '') 
      }
    }
  },
  test: {
      globals: true,
      environment: 'jsdom',
      css: true,
  }
})

