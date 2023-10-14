import React, { useEffect, useState } from 'react'

import { useDispatch, useSelector } from 'react-redux'
import { NavLink, useSearchParams } from 'react-router-dom'

import { getCategories } from '../../features/categories/categoriesSlice'
import { AppDispatch } from '../../features/store'
import styles from '../../styles/Sidebar.module.css'
import { ROUTES } from '../../utils/routes'

export const Sidebar = () => {
  const { list } = useSelector(({ categories }) => categories)

  const dispatch = useDispatch<AppDispatch>()

  const [searchParams] = useSearchParams()
  const [currentCategory, setCurrentCategory] = useState(searchParams.get('category'))

  useEffect(() => {
    dispatch(getCategories())
  }, [dispatch])

  useEffect(() => {
    setCurrentCategory(searchParams.get('category'))
  }, [searchParams])

  return (
    <section className={styles.sidebar}>
      <div className={styles.title}>КАТЕГОРИИ</div>
      <nav>
        <ul className={styles.menu}>
          {list.slice(0, 9).map(({ id, name }: any) => (
            <li key={id}>
              <NavLink
                className={() => `${styles.link} ${id == currentCategory ? styles.active : ''}`}
                to={`${ROUTES.ORDERS}/?category=${id}`}
              >
                {name}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
    </section>
  )
}
