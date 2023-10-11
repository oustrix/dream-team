import React from 'react';
import { AppRoutes } from './components/Routes/Routes';
import { Header } from './components/Header/Header';
import { Footer } from './components/Footer/Footer';
import { Sidebar } from './components/Sidebar/Sidebar';

function App() {
  return (
    <div className="app">
      <Header />
      <AppRoutes />
      <Sidebar />
      <Footer />
    </div>
  );
}

export default App;
