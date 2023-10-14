import { configureStore } from '@reduxjs/toolkit'

import categoriesSlice from './categories/categoriesSlice'
import posterSlice from './poster/posterSlice'

export const store = configureStore({
  reducer: {
    categories: categoriesSlice,
    poster: posterSlice,
  },
  devTools: true,
})

export type AppDispatch = typeof store.dispatch
