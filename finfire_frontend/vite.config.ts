import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// Multi-tenant aware dev config:
//  - host: true  → bind on 0.0.0.0 so *.localhost resolves to the dev server
//  - allowedHosts: true → accept Host headers like "acme.localhost"
//  - proxy /api with changeOrigin: false so the original Host (e.g. acme.localhost)
//    is forwarded to Django, letting django_tenants resolve the active tenant.
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    host: true,
    port: 5173,
    allowedHosts: true,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: false,
      },
      '/auth': {
        target: 'http://localhost:8000',
        changeOrigin: false,
      },
      '/admin': {
        target: 'http://localhost:8000',
        changeOrigin: false,
      },
      '/static': {
        target: 'http://localhost:8000',
        changeOrigin: false,
      },
      '/media': {
        target: 'http://localhost:8000',
        changeOrigin: false,
      },
    },
  },
})
