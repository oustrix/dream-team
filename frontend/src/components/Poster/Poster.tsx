import React, { useEffect } from 'react'

import { useDispatch, useSelector } from 'react-redux'

import { getPoster } from '../../features/poster/posterSlice'
import { AppDispatch } from '../../features/store'
import styles from '../../styles/Poster.module.css'

export const Poster = () => {
  const { url } = useSelector(({ poster }) => poster)
  const dispatch = useDispatch<AppDispatch>()

  useEffect(() => {
    dispatch(getPoster())
  }, [dispatch])

  return (
    <section className={styles.poster}>
      <div className={styles.image}>
        <img src={`${url}`} alt='' />
      </div>
    </section>
  )
}
