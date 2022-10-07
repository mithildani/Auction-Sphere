import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Button } from "reactstrap";
import axios from "axios";

import AddBid from "./AddBid";
import Footer from "./Footer";
import Navv from "./Navv";
import { URL } from "../global";

const ProductDetails = () => {
  let { id } = useParams();
  const [showAddBid, setShowAddBid] = useState(false);
  const [showButton, setShowButton] = useState(false);
  const [bids, setBids] = useState([]);
  const [product, setProduct] = useState(null);
  const getProductDetails = async () => {
    try {
      let data = await axios.post(`${URL}/product/getDetails`, {
        productID: id,
      });
      console.log(data);
      setBids(data.data.bids);
      setProduct(data.data.product[0]);
    } catch (error) {
      alert("Something went wrong");
    }
  };
  useEffect(() => {
    getProductDetails();
    if (typeof window !== "undefined") {
      if (localStorage.getItem("auth") === "true") {
        setShowButton(true);
      }
    }
  }, []);
  return (
    <>
      <Navv />
      <p>Details page for product id {id} </p>
      {product && (
        <div>
          <p>Product ID: {product[0]} </p>
          <p>Product Name: {product[1]} </p>
          <p>Image: {product[2]} </p>
          <p>Seller: {product[3]} </p>
          <p>Minimum price {product[4]} </p>
          <p>Date posted: {product[5]} </p>
          <p>Bidding window closes on: {product[7]} </p>
          <p>Minimum price increment to beat a bid: {product[6]} </p>
          <p>Product Description: {product[8]} </p>
        </div>
      )}
      {showButton && (
        <>
          <Button color="info" onClick={() => setShowAddBid(!showAddBid)}>
            {showAddBid ? <span>-</span> : <span>+</span>} Add a Bid
          </Button>
          {showAddBid && <AddBid productId={id} />}
        </>
      )}
      <Footer />
    </>
  );
};

export default ProductDetails;
