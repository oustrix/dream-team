import React, { useEffect } from 'react'

import { useDispatch, useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom'

import { getCategories } from '../../features/categories/categoriesSlice'
import { AppDispatch } from '../../features/store'
import styles from '../../styles/Sidebar.module.css'
import { ROUTES } from '../../utils/routes'

export const Sidebar = () => {
  const { list } = useSelector(({ categories }) => categories)

  const dispatch = useDispatch<AppDispatch>()

  useEffect(() => {
    dispatch(getCategories())
  }, [dispatch])
  return (
    <section className={styles.sidebar}>
      <div className={styles.title}>КАТЕГОРИИ</div>
      <nav>
        <ul className={styles.menu}>
          {list.map(({ id, name }: any) => (
            <li key={id}>
              <NavLink to={`${ROUTES.ORDERS}/?category=${id}`}>{name}</NavLink>
            </li>
          ))}
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
