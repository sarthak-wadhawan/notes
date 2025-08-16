import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { inject } from '@vercel/analytics'
import App from './App.jsx'
import { Analytics } from '@vercel/analytics/react'
// Initialize analytics (runs once when app loads)
inject()

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Analytics />
    <App />
  </StrictMode>
)