import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-section">
          <h4>About Us</h4>
          <p>Empowering mental health professionals with ethical AI to transform trauma recovery for children globally.</p>
        </div>
            {/* <div className="footer-section">
            <h4>Contact</h4>
            <p>Email: info@2ts.ai</p>
            <p>Phone: (123) 456-7890</p>
            </div> */}
        <div className="footer-section">
          <h4>Follow Us</h4>
          {/* <div className="social-icons">
            <a href="https://twitter.com/2tsai" target="_blank" rel="noopener noreferrer">Twitter</a>
            <a href="https://linkedin.com/company/2tsai" target="_blank" rel="noopener noreferrer">LinkedIn</a>
          </div> */}
        </div>
      </div>
      <div className="footer-bottom">
        <p>&copy; 2024 2Ts.ai. All rights reserved.</p>
      </div>
    </footer>
  );
}

export default Footer;
