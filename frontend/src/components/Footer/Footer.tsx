import React from 'react'
import { Link } from 'react-router-dom'

import LOGO from '../../images/logo.svg'
import styles from '../../styles/Footer.module.css'

import { ROUTES } from '../../utils/routes'

export const Footer = () => {
  return (
    <section className={styles.footer}>
      <div className={styles.logo}>
        <Link to={ROUTES.HOME}>
          <img src={LOGO} alt='W4F' />
        </Link>
      </div>
    </section>
  )
}
