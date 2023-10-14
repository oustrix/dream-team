import React from 'react'
import { Link } from 'react-router-dom'

import LOGO from '../../images/logo.svg'
import styles from '../../styles/Footer.module.css'

import { ROUTES } from '../../utils/routes'

export const Footer = () => {
  return (
    <section className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.logo}>
          <Link to={ROUTES.HOME}>
            <img src={LOGO} alt='W4F' />
          </Link>
        </div>

        <a href='/help' target='_blank' className={styles.link}>
          Полезные советы и ресурсы
        </a>
      </div>

      <div className={styles.rights}>
        Developed for ITaP{' '}
        <a href='https://youtu.be/XfqOB4hvxlY' target='_blank' rel='noreferrer'>
          ♥
        </a>
      </div>

      <div className={styles.container}>
        <a href='/terms' target='_blank' className={styles.link}>
          Пользовательское соглашение
        </a>

        <div className={styles.socials}>
          <a href='https://github.com/oustrix/itip-project' target='_blank' rel='noreferrer'>
            <svg className='icon' width='24px' height='24px'>
              <use xlinkHref={`${process.env.PUBLIC_URL}/sprite.svg#github`} />
            </svg>
          </a>
        </div>
      </div>
    </section>
  )
}
