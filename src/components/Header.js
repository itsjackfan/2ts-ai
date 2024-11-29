import React from 'react';
import './Header.css';
import logo from './logo.png'; // Replace with your logo path

function Header() {
  return (
    <header className="header">
      {/* Logo Section */}
      <div className="header-left">
        <img src={logo} alt="2Ts.ai Logo" className="header-logo" />
      </div>

      {/* Navigation Links
      <nav className="header-nav">
        <a href="#why-us" className="header-link">Why Us?</a>
        <a href="#solutions" className="header-link">Solutions</a>
        <a href="#resources" className="header-link">Resources</a>
        <a href="#pricing" className="header-link">Pricing</a>
      </nav> */}
    </header>
  );
}

export default Header;
