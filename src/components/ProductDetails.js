import React, { useState } from "react";
import { useParams } from "react-router-dom";
import AddBid from "./AddBid";
import Footer from "./Footer";
import Navv from "./Navv";
import { Button } from "reactstrap";

const ProductDetails = () => {
  let { id } = useParams();
  return (
    <>
      <Navv />
      <p>Details page for product id {id} </p>
      <Button color="info" href="/bid">
        + Add a Bid
      </Button>
      <Footer />
    </>
  );
};

export default ProductDetails;
