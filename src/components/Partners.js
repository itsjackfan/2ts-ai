import React from 'react';
import './Partners.css';
import partner1 from "./partner1.png";
import partner2 from "./partner2.png";

function Partners() {
  return (
    <section className="partners">
      <h2>Our Partners</h2>
      <div className="partners-logos">
        <img src={partner1} alt="Partner 1" />
        <img src={partner2} alt="Partner 2" />
      </div>
    </section>
  );
}

export default Partners;
