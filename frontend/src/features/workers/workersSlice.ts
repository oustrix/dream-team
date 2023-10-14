import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import axios from 'axios'

import { BASE_URL } from '../../utils/constants'

export const getWorkers = createAsyncThunk('workers/getWorkers', async (_, thunkAPI) => {
  try {
    const res = await axios(`${BASE_URL}/users/?kind=worker&amount=9`)
    return res.data
  } catch (err) {
    console.log(err)
    return thunkAPI.rejectWithValue(err)
  }
})

const workersSlice = createSlice({
  name: 'workers',
  initialState: {
    list: [],
    isLoading: false,
  },
  extraReducers: (builder) => {
    builder.addCase(getWorkers.pending, (state) => {
      state.isLoading = true
    })
    builder.addCase(getWorkers.fulfilled, (state, { payload }) => {
      state.list = payload
      state.isLoading = false
    })
    builder.addCase(getWorkers.rejected, (state) => {
      state.isLoading = false
    })
  },
  reducers: {},
})

export default workersSlice.reducer
