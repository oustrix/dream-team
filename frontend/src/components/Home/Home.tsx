import React from 'react'

import styles from '../../styles/Home.module.css'
import { Poster } from '../Poster/Poster'
import { Sidebar } from '../Sidebar/Sidebar'

export const Home = () => {
  return (
    <div>
      <div className={styles.header}>
        <Sidebar />
        <Poster />
      </div>
    </div>
  )
}
