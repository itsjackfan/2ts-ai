import React, { useState, useEffect } from 'react';
import './HeroSection.css';

function HeroSection() {
  const [fadeIn, setFadeIn] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setFadeIn(true), 500); // Delay animation start
    return () => clearTimeout(timer); // Clean up timer
  }, []);

  return (
    <div className={`hero-container ${fadeIn ? 'fade-in' : ''}`}>
      <h1 className="hero-title">Training the Next  Trainer.</h1>
      <p className="hero-subtitle">
        Using the power of agentic simulation to give mental health professionals 
        unprecedented access to best practices, collaborative forums, and therapy practice.
      </p>
      <div className="hero-buttons">
        <button
          className="hero-button"
          onClick={() => window.open('https://drive.google.com/file/d/1ScH9a43BCEpl7XDP2O3uyymBfmkuasY2/view?usp=drive_link', '_blank')}
        >
          Read our whitepaper
        </button>
      </div>
    </div>
  );
}

export default HeroSection;
