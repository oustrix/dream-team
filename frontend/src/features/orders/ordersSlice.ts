import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'

import axios from 'axios'

import { BASE_URL } from '../../utils/constants'

export interface OrderRequest {
  categoryID: string | null
  page: string | null
}

export const getOrders = createAsyncThunk('orders/getOrders', async (ordersRequest: OrderRequest, thunkAPI) => {
  const { categoryID, page } = ordersRequest
  const requestURL = new URL(`${BASE_URL}/orders`)

  if (categoryID) {
    requestURL.searchParams.append('category', categoryID)
  }
  if (page) {
    requestURL.searchParams.append('page', page)
  }

  try {
    const res = await axios(requestURL.toString())
    return res.data
  } catch (err) {
    console.log(err)
    return thunkAPI.rejectWithValue(err)
  }
})

const ordersSlice = createSlice({
  name: 'orders',
  initialState: {
    list: [],
    isLoading: false,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(getOrders.pending, (state) => {
      state.isLoading = true
    })
    builder.addCase(getOrders.fulfilled, (state, { payload }) => {
      state.list = payload
      state.isLoading = false
    })
    builder.addCase(getOrders.rejected, (state) => {
      state.isLoading = false
    })
  },
})

export default ordersSlice.reducer
