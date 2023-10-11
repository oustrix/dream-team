import React from 'react'

import { NavLink } from 'react-router-dom'

import styles from '../../styles/Sidebar.module.css'
import { ROUTES } from '../../utils/routes'

export const Sidebar = () => {
  return (
    <section className={styles.sidebar}>
      <div className={styles.title}>КАТЕГОРИИ</div>
      <nav>
        <ul className={styles.menu}>
          <li id=''>
            <NavLink to={`${ROUTES.ORDERS}/?category=`}>Link</NavLink>
          </li>
        </ul>
      </nav>

      <div className={styles.footer}>
        <a href='/help' target='_blank' className={styles.link}>
          Помощь
        </a>
        <a href='/terms' target='_blank' className={styles.link} style={{ textDecoration: 'underline' }}>
          Пользовательское соглашение
        </a>
      </div>
    </section>
  )
}
