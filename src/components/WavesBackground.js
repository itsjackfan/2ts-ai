import React, { useState, useEffect } from 'react';
import './WavesBackground.css';

function WavesBackground() {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => setVisible(true), 300); // Delay background fade-in
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className={`waves-background ${visible ? 'fade-in' : ''}`}></div>
  );
}

export default WavesBackground;
