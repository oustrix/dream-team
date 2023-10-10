import React from 'react'

import { Route, Routes } from 'react-router-dom'

import { Home } from '../Home/Home'

export const AppRoutes = () => {
  return (
    <Routes>
      <Route index element={<Home />} />
    </Routes>
  )
}

export default AppRoutes
