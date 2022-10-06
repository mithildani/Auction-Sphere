import React from "react";

const Footer = () => {
  return (
    <div
      style={{
        position: "fixed",
        bottom: "0",
        width: "100%",
      }}
      className="footer"
    >
      <div className="container">
        <div className="row">
          <hr />
          <p>
            One stop portal for auctioning and selling items. Created by Tanvi
            Sinha, Kartik Soni, Palash Rathod, Shreya Maheshwari, and Nandini
            Mundra.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Footer;
