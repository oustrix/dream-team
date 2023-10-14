import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import axios from 'axios'

import { BASE_URL } from '../../utils/constants'

export const getPosters = createAsyncThunk('posters/getPosters', async (_, thunkAPI) => {
  try {
    const res = await axios(`${BASE_URL}/posters`)
    return res.data
  } catch (err) {
    console.log(err)
    return thunkAPI.rejectWithValue(err)
  }
})

const postersSlice = createSlice({
  name: 'posters',
  initialState: {
    list: [],
    isLoading: true,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(getPosters.pending, (state) => {
      state.isLoading = true
    })
    builder.addCase(getPosters.fulfilled, (state, { payload }) => {
      state.list = payload
      state.isLoading = false
    })
    builder.addCase(getPosters.rejected, (state) => {
      state.isLoading = false
    })
  },
})

export default postersSlice.reducer
