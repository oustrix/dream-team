import React, { useEffect, useRef, useState } from 'react'

import ReactDOM from 'react-dom/client'
import { useDispatch, useSelector } from 'react-redux'

import { NavLink, useSearchParams } from 'react-router-dom'

import { getCategories } from '../../features/categories/categoriesSlice'
import { getOrders, OrderRequest } from '../../features/orders/ordersSlice'
import { getPaybacks } from '../../features/paybacks/paybacksSlice'
import { AppDispatch } from '../../features/store'
import styles from '../../styles/Orders.module.css'

export const Orders = ({ amount }: { amount: number }) => {
  const orders = useSelector(({ orders }) => orders)
  const categories = useSelector(({ categories }) => categories)
  const paybacks = useSelector(({ paybacks }) => paybacks)

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
    dispatch(getCategories())
    dispatch(getPaybacks())
  }, [dispatch, searchParams, amount])

  const showCategoriesList = () => {
    let list = document!.getElementById('categories_list')
    // @ts-ignore
    list.style.display = 'block'
  }

  const hideCategoriesList = () => {
    let list = document!.getElementById('categories_list')
    // @ts-ignore
    list.style.display = 'none'
  }

  // @ts-ignore
  const useOutsideCategories = (ref) => {
    useEffect(() => {
      // @ts-ignore
      function handleClickOutside(event) {
        if (ref.current && !ref.current.contains(event.target)) {
          hideCategoriesList()
        }
      }

      document.addEventListener('mousedown', handleClickOutside)
      return () => {
        document.removeEventListener('mousedown', handleClickOutside)
      }
    }, [ref])
  }

  const wrapperCategoriesRef = useRef(null)
  useOutsideCategories(wrapperCategoriesRef)

  const [selectedCategories, setSelectedCategories] = useState<number[]>([])

  const addCategory = (id: number, name: string) => {
    if (selectedCategories.includes(id)) {
      hideCategoriesList()
      return
    }

    const category_wrapper = document.createElement('div')
    document.getElementById('categories_box')?.append(category_wrapper)
    const category = (
      <div className={styles.selected} id={`category-${id.toString()}`}>
        {name}
        <svg className={styles.close} onClick={() => removeCategory(id)} width='16px' height='16px'>
          <use xlinkHref={`${process.env.PUBLIC_URL}/sprite.svg#close`} />
        </svg>
      </div>
    )

    const wrap = ReactDOM.createRoot(category_wrapper)
    setSelectedCategories((selectedCategories) => [...selectedCategories, id])
    wrap.render(category)
    hideCategoriesList()
  }

  const removeCategory = (id: number) => {
    setSelectedCategories((selectedCategories) => selectedCategories.filter((selectedID) => selectedID !== id))

    document.getElementById('category-' + id.toString())?.remove()
  }

  const [selectedPaybacks, setSelectedPaybacks] = useState<number[]>([])

  const showPaybacksList = () => {
    let list = document!.getElementById('paybacks_list')

    // @ts-ignore
    list.style.display = 'block'
  }

  const hidePaybacksList = () => {
    let list = document!.getElementById('paybacks_list')
    // @ts-ignore
    list.style.display = 'none'
  }

  // @ts-ignore
  const useOutsidePaybacks = (ref) => {
    useEffect(() => {
      // @ts-ignore
      function handleClickOutside(event) {
        if (ref.current && !ref.current.contains(event.target)) {
          hidePaybacksList()
        }
      }

      document.addEventListener('mousedown', handleClickOutside)
      return () => {
        document.removeEventListener('mousedown', handleClickOutside)
      }
    }, [ref])
  }

  const addPayback = (id: number, name: string) => {
    if (selectedPaybacks.includes(id)) {
      hidePaybacksList()
      return
    }

    const category_wrapper = document.createElement('div')
    document.getElementById('paybacks_box')?.append(category_wrapper)
    const payback = (
      <div className={styles.selected} id={`payback-${id.toString()}`}>
        {name}
        <svg className={styles.close} onClick={() => removePayback(id)} width='16px' height='16px'>
          <use xlinkHref={`${process.env.PUBLIC_URL}/sprite.svg#close`} />
        </svg>
      </div>
    )

    const wrap = ReactDOM.createRoot(category_wrapper)
    setSelectedPaybacks((selectedPaybacks) => [...selectedPaybacks, id])
    wrap.render(payback)
    hidePaybacksList()
  }

  const removePayback = (id: number) => {
    setSelectedPaybacks((selectedPaybacks) => selectedPaybacks.filter((selectedID) => selectedID !== id))

    document.getElementById('payback-' + id.toString())?.remove()
  }

  const wrapperPaybacksRef = useRef(null)
  useOutsidePaybacks(wrapperPaybacksRef)

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
            <div ref={wrapperCategoriesRef}>
              <div className={styles.select} onClick={showCategoriesList}>
                <input type='text' placeholder='Выберите категорию' className={styles.input} />
                <div className={styles.arrow}>
                  <svg width='16px' height='16px'>
                    <use xlinkHref={`${process.env.PUBLIC_URL}/sprite.svg#arrow`} />
                  </svg>
                </div>
              </div>
              <ul className={styles.list} id='categories_list' style={{ display: 'none' }}>
                {categories.list.map(({ id, name }: { id: number; name: string }) => (
                  <li key={id} className={styles.list_option} id={id.toString()} onClick={() => addCategory(id, name)}>
                    {name}
                  </li>
                ))}
              </ul>
              <div className={styles.categories_box} id='categories_box'></div>
            </div>
          </div>
          <div className={styles.config_food}>
            <h3 className={styles.config_header}>Способ оплаты</h3>
            <div ref={wrapperPaybacksRef}>
              <div className={styles.select} onClick={showPaybacksList}>
                <input type='text' placeholder='Выберите способ оплаты' className={styles.input} />
                <div className={styles.arrow}>
                  <svg width='16px' height='16px'>
                    <use xlinkHref={`${process.env.PUBLIC_URL}/sprite.svg#arrow`} />
                  </svg>
                </div>
              </div>
              <ul className={styles.list} id='paybacks_list' style={{ display: 'none' }}>
                {paybacks.list.map(
                  ({
                    id,
                    name,
                    count,
                    units,
                    price,
                  }: {
                    id: number
                    name: string
                    count: number
                    units: string
                    price: number
                  }) => (
                    <li key={id} className={styles.list_option} id={id.toString()} onClick={() => addPayback(id, name)}>
                      <p style={{ display: 'inline-block' }}>{name}</p>
                      <p style={{ display: 'inline-block' }}>
                        {count} {units}
                      </p>
                    </li>
                  ),
                )}
              </ul>
              <div className={styles.paybacks_box} id='paybacks_box'></div>
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
