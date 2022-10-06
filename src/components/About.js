import React from "react";
import Navv from "./Navv";
import logo from "../assets/Logo.png";

const About = () => {
  return (
    <>
      <Navv />
      <h1>About Auction-Sphere</h1>
      <p>
        Auction Sphere is an auctioning system where people can bid on exciting
        items and also put items up for sale. Every item has a bidding window,
        and the item goes to the highest bidder by the end of that window.
      </p>
      <img src={logo} style={{ height: 400, width: 530 }} />
      <br />
      <div style={{ mariginTop: "5rem" }}>
        On the homepage, people can view all the latest items being put up for
        sale and their respective highest bids. On the product details page,
        apart from product details, people can view the latest bids as well as
        the highest bid, and can also place a bid. It's upto the seller to
        decide the minimum price of the product, as well as bid increments.
      </div>
    </>
  );
};

export default About;
