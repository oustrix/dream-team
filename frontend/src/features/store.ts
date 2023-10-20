import { configureStore } from '@reduxjs/toolkit'

import categoriesSlice from './categories/categoriesSlice'
import ordersSlice from './orders/ordersSlice'
import workersSlice from './workers/workersSlice'

export const store = configureStore({
  reducer: {
    categories: categoriesSlice,
    workers: workersSlice,
    orders: ordersSlice,
  },
  devTools: true,
})

export type AppDispatch = typeof store.dispatch
