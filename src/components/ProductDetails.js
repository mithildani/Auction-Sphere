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
  const getProductDetails = async () => {
    let data = await axios.get(`${URL}/product/getDetails`, { productID: id });
    console.log(data);
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
