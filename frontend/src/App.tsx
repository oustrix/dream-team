import React from 'react';
import { AppRoutes } from './components/Routes/Routes';
import { Header } from './components/Header/Header';
import { Footer } from './components/Footer/Footer';

function App() {
  return (
    <div className="App">
      <Header />
      <AppRoutes />
      <Footer />
    </div>
  );
}

export default App;
