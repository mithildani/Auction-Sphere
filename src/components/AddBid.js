import React, { useState } from "react";
import { Form, FormGroup, Label, Input, Navbar, Button } from "reactstrap";

const AddBid = ({ productId }) => {
  const [amount, setAmount] = useState(0);
  const handleChange = (event) => {
    setAmount(event.target.value);
  };
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(amount);
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
