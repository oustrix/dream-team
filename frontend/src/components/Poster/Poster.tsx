import React, { useEffect } from 'react'

import BG from '../../images/nutella.png'
import styles from '../../styles/Poster.module.css'

export const Poster = () => {
  return (
    <section className={styles.poster}>
      <div className={styles.title}>ЛУЧШИЕ ИСПОЛНИТЕЛИ</div>
      <div style={{ display: 'flex' }}>
        <div className={styles.product}>
          <div className={styles.subtitle}>КРУПНЕЙШАЯ БИРЖА</div>
          <h1 className={styles.head}>БЫСТРОЕ ВЫПОЛНЕНИЕ</h1>
          <button className={styles.button}>Разместить заказ</button>
        </div>
        <div className={styles.image}>
          <img src={BG} alt='' />
        </div>
      </div>
    </section>
  )
}
