import React from 'react';
import WavesBackground from './components/WavesBackground';
import HeroSection from './components/HeroSection';
import Footer from './components/Footer';
import Partners from './components/Partners';
import './App.css';
import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <WavesBackground />
      <Header />
      <HeroSection />
      <Partners />
      <Footer />
    </div>
  );
}

export default App;
