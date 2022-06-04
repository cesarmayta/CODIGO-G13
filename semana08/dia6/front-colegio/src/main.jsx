import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import Auth from './pages/Auth'
import './css/styles.css'

import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<Auth />} />
      <Route path="main" element={<App />} />
    </Routes>
  </BrowserRouter>
)
