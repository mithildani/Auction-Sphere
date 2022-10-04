import React, { useState } from "react";
import { useParams } from "react-router-dom";
import AddBid from "./AddBid";
import Footer from "./Footer";
import Navv from "./Navv";
import { Button } from "reactstrap";

const ProductDetails = () => {
  let { id } = useParams();
  const [showAddBid, setShowAddBid] = useState(false);
  return (
    <>
      <Navv />
      <p>Details page for product id {id} </p>
      <Button color="info" onClick={() => setShowAddBid(!showAddBid)}>
        {showAddBid ? <span>-</span> : <span>+</span>} Add a Bid
      </Button>
      {showAddBid && <AddBid />}
      <Footer />
    </>
  );
};

export default ProductDetails;
