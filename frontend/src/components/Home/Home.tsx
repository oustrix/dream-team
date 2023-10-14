import React, { useEffect } from 'react'

import { useDispatch, useSelector } from 'react-redux'

import { AppDispatch } from '../../features/store'
import { getWorkers } from '../../features/workers/workersSlice'
import { BestWorkers } from '../BestWorkers/BestWorkers'
import { Poster } from '../Poster/Poster'
import { Sidebar } from '../Sidebar/Sidebar'

export const Home = () => {
  const dispatch = useDispatch<AppDispatch>()

  useEffect(() => {
    dispatch(getWorkers())
  }, [dispatch])

  const workers = useSelector(({ workers }) => workers).list

  return (
    <div>
      <div style={{ display: 'flex' }}>
        <Sidebar />
        <Poster />
      </div>
      <BestWorkers workers={workers} amount={8} />
    </div>
  )
}
