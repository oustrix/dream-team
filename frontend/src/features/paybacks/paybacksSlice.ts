import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import axios from 'axios'

import { BASE_URL } from '../../utils/constants'

export const getPaybacks = createAsyncThunk('paybacks/getPaybacks', async (_, thunkAPI) => {
  try {
    const res = await axios(`${BASE_URL}/paybacks/`)
    return res.data
  } catch (err) {
    console.log(err)
    return thunkAPI.rejectWithValue(err)
  }
})

const paybacksSlice = createSlice({
  name: 'paybacks',
  initialState: {
    list: [],
    isLoading: false,
  },
  extraReducers: (builder) => {
    builder.addCase(getPaybacks.pending, (state) => {
      state.isLoading = true
    })
    builder.addCase(getPaybacks.fulfilled, (state, { payload }) => {
      state.list = payload
      state.isLoading = false
    })
    builder.addCase(getPaybacks.rejected, (state) => {
      state.isLoading = false
    })
  },
  reducers: {},
})

export default paybacksSlice.reducer
