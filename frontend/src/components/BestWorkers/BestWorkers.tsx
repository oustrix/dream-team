import React from 'react'
import { Link } from 'react-router-dom'

import styles from '../../styles/BestWorkers.module.css'
import { ROUTES } from '../../utils/routes'

export const BestWorkers = ({ workers = [], amount }: { workers: []; amount: number }) => {
  const list = workers.filter((_, i) => i < amount)

  return (
    <section className={styles.workers}>
      <h2>Лучшие исполнители</h2>
      <div className={styles.list}>
        {list.map(({ id, image, name, category }) => (
          <Link to={`${ROUTES.USERS}/${id}`} key={id} className={styles.worker}>
            <div className={styles.user}>
              <div className={styles.avatar}>
                <img src={image} alt={name} />
              </div>

              <div className={styles.user_info}>
                <div className={styles.name}>{name}</div>
                <div className={styles.category}>{category}</div>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </section>
  )
}
