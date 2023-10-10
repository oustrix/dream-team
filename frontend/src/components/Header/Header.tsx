import React from 'react'
import { Link } from 'react-router-dom'

import LOGO from '../../images/logo.svg'
import styles from '../../styles/Header.module.css'
import { ROUTES } from '../../utils/routes'

export const Header = () => {
  return (
    <div className={styles.header}>
      <div className={styles.logo}>
        <Link to={ROUTES.HOME}>
          <img src={LOGO} alt='TASK HUB' />
        </Link>
      </div>
    </div>
  )
}
