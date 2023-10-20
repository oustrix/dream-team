import React from 'react'

import { Route, Routes } from 'react-router-dom'

import { Home } from '../Home/Home'
import { Orders } from '../Orders/Orders'

export const AppRoutes = () => {
  return (
    <Routes>
      <Route index element={<Home />} />
      <Route path='/orders' element={<Orders amount={20} />} />
    </Routes>
  )
}

export default AppRoutes
