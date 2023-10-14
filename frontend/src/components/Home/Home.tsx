import React from 'react'

import { Poster } from '../Poster/Poster'
import { Sidebar } from '../Sidebar/Sidebar'

export const Home = () => {
  return (
    <div>
      <div>
        <Sidebar />
        <Poster />
      </div>
    </div>
  )
}
