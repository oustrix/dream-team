import { configureStore } from '@reduxjs/toolkit'

import categoriesSlice from './categories/categoriesSlice'
import workersSlice from './workers/workersSlice'
import ordersSlice from './orders/ordersSlice'

export const store = configureStore({
  reducer: {
    categories: categoriesSlice,
    workers: workersSlice,
    orders: ordersSlice,
  },
  devTools: true,
})

export type AppDispatch = typeof store.dispatch
