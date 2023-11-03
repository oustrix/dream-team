import { configureStore } from '@reduxjs/toolkit'

import categoriesSlice from './categories/categoriesSlice'
import ordersSlice from './orders/ordersSlice'
import paybacksSlice from './paybacks/paybacksSlice'
import workersSlice from './workers/workersSlice'

export const store = configureStore({
  reducer: {
    categories: categoriesSlice,
    workers: workersSlice,
    orders: ordersSlice,
    paybacks: paybacksSlice,
  },
  devTools: true,
})

export type AppDispatch = typeof store.dispatch
