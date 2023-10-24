import React, { useEffect } from 'react'

import { useDispatch, useSelector } from 'react-redux'

import { NavLink, useSearchParams } from 'react-router-dom'

import { getOrders, OrderRequest } from '../../features/orders/ordersSlice'
import { AppDispatch } from '../../features/store'
import styles from '../../styles/Orders.module.css'

export const Orders = ({ amount }: { amount: number }) => {
  const orders = useSelector(({ orders }) => orders)

  const dispatch = useDispatch<AppDispatch>()

  const [searchParams] = useSearchParams()

  useEffect(() => {
    let req: OrderRequest = {
      categoryID: searchParams.get('category'),
      page: searchParams.get('page') ? searchParams.get('page') : '1',
      amount: searchParams.get('amount') ? searchParams.get('amount') : amount.toString(),
      status: 'open',
    }
    dispatch(getOrders(req))
  }, [dispatch, searchParams, amount])

  return (
    <div>
      <div className={styles.container}>
        <section className={styles.orders_container}>
          <div className={styles.header}>
            <h1>Заказы</h1>
          </div>
          <div className={styles.orders}>
            {orders.list.map(({ id, title, description }: { id: number; title: string; description: string }) => (
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
        <section className={styles.config}>
          <div className={styles.config_categories}>
            <h3 className={styles.config_header}>Категория</h3>
            <div className={styles.select}>
              <input type='text' placeholder='Выберите категорию' className={styles.input} />
              <div className={styles.arrow}>
                <svg width='16px' height='16px'>
                  <use xlinkHref={`${process.env.PUBLIC_URL}/sprite.svg#arrow`} />
                </svg>
              </div>
            </div>
          </div>
          <div className={styles.config_food}>
            <h3 className={styles.config_header}>Способ оплаты</h3>
            <div className={styles.select}>
              <input type='text' placeholder='Выберите способ оплаты' className={styles.input} />
              <div className={styles.arrow}>
                <svg width='16px' height='16px'>
                  <use xlinkHref={`${process.env.PUBLIC_URL}/sprite.svg#arrow`} />
                </svg>
              </div>
            </div>
          </div>
          <div className={styles.config_confirm}>
            <button>Применить фильтры</button>
          </div>
        </section>
      </div>
    </div>
  )
}
