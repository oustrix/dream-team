import React, { useEffect } from 'react'

import { useDispatch, useSelector } from 'react-redux'

import { NavLink, useSearchParams } from 'react-router-dom'

import { getOrders, OrderRequest } from '../../features/orders/ordersSlice'
import { AppDispatch } from '../../features/store'
import styles from '../../styles/Orders.module.css'

export const Orders = ({ amount }: { amount: number }) => {
  const { list } = useSelector(({ orders }) => orders)

  const dispatch = useDispatch<AppDispatch>()

  const [searchParams] = useSearchParams()

  useEffect(() => {
    let req: OrderRequest = {
      categoryID: searchParams.get('category'),
      page: searchParams.get('page') ? searchParams.get('page') : '1',
      amount: searchParams.get('amount') ? searchParams.get('amount') : amount.toString(),
    }
    dispatch(getOrders(req))
  }, [dispatch, searchParams, amount])

  return (
    <div className={styles.container}>
      <section className={styles.orders_container}>
        <div className={styles.header}>
          <h1>Заказы</h1>
        </div>
        <div className={styles.orders}>
          {list.map(({ id, title, description }: { id: number; title: string; description: string }) => (
            <div key={id} className={styles.order}>
              <div className={styles.info}>
                <NavLink to={`${id}`} className={styles.link}>
                  <h2 className={styles.order_title}>{title}</h2>
                </NavLink>
                <div className={styles.description}>{description}</div>
              </div>
            </div>
          ))}
        </div>
      </section>
      <section className={styles.config}>конфиг</section>
    </div>
  )
}
