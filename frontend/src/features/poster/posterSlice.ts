import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import axios from 'axios'

import { BASE_URL } from '../../utils/constants'

export const getPoster = createAsyncThunk('poster/getPoster', async (_, thunkAPI) => {
  try {
    const res = await axios(`${BASE_URL}/poster`)
    return res.data
  } catch (err) {
    console.log(err)
    return thunkAPI.rejectWithValue(err)
  }
})

const posterSlice = createSlice({
  name: 'poster',
  initialState: {
    url: '',
    isLoading: true,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(getPoster.pending, (state) => {
      state.isLoading = true
    })
    builder.addCase(getPoster.fulfilled, (state, { payload }) => {
      state.url = payload
      state.isLoading = false
    })
    builder.addCase(getPoster.rejected, (state) => {
      state.isLoading = false
    })
  },
})

export default posterSlice.reducer
