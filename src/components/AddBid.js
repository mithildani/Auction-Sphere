import React, { useState } from "react";
import { Form, FormGroup, Label, Input, Navbar, Button } from "reactstrap";
import axios from "axios";
import { URL } from "../global";

const AddBid = ({ productId }) => {
  const [amount, setAmount] = useState(0);
  const handleChange = (event) => {
    setAmount(event.target.value);
  };
  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(amount);
    let response;
    try {
      if (typeof window !== "undefined") {
        response = await axios.post(`${URL}/bid/create`, {
          bidAmount: amount,
          prodId: productId,
          email: localStorage.getItem("email"),
        });
        console.log(response);
      }
    } catch (e) {
      console.log(e);
      alert(e.response.data);
    }
  };
  return (
    <>
      AddBid for {productId}
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for="amount">Amount</Label>
          <Input
            id="amount"
            name="amount"
            placeholder="Enter your bid amount here"
            type="amount"
            value={amount}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <Button color="primary">Submit</Button>
      </Form>
    </>
  );
};

export default AddBid;
