import React, { useState } from "react";
import { useParams } from "react-router-dom";
import Footer from "./Footer";
import Navv from "./Navv";

const ProductDetails = () => {
  let { id } = useParams();
  return (
    <>
      <Navv />
      <p>Details page for product id {id} </p>
      <Footer />
    </>
  );
};

export default ProductDetails;
