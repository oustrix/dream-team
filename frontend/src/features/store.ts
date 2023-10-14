import { configureStore } from '@reduxjs/toolkit'

import categoriesSlice from './categories/categoriesSlice'
import postersSlice from './posters/postersSlice'

export const store = configureStore({
  reducer: {
    categories: categoriesSlice,
    posters: postersSlice,
  },
  devTools: true,
})

export type AppDispatch = typeof store.dispatch
