import React from 'react'
import ReactDOM from 'react-dom/client'
import { Provider } from 'react-redux'

import './styles/index.css'
import { BrowserRouter } from 'react-router-dom'

import App from './App'
import { store } from './features/store'

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement)
root.render(
  <Provider store={store}>
    <React.StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </React.StrictMode>
  </Provider>,
)
