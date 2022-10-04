import React, { useState, useCallback } from "react";
import { Form, FormGroup, Label, Input, Navbar, Button } from "reactstrap";
import Navv from "./Navv";
import Footer from "./Footer";

const toBase64 = (file) =>
  new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (event) => {
      resolve(event.target.result);
    };
    reader.onerror = (error) => {
      reject(error);
    };

    reader.readAsDataURL(file);
  });

const Sell = () => {
  const [encodedImages, setEncodedImages] = useState();
  const handleChange = (event) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    //formData.email = localStorage.getItem('email');
    formData.encodedImages = encodedImages;
    console.log(formData);
    //Set local storage
    // if(api.response == success)
    //   localStorage.setItem("auth", true);
  };

  const [formData, setFormData] = useState({
    pname: "",
    initialPrice: "",
    increment: "",
    datePosted: Date.now(),
    description: "",
    biddingTime: "",
  });

  const handleFileInputChange = useCallback(async (acceptedFiles) => {
    for (let i = 0; i < acceptedFiles.target.files.length; i++) {
      let file = acceptedFiles.target.files[i];
      console.log(file);
      let base64EncodedImage = await toBase64(file);
      setEncodedImages(base64EncodedImage);
      console.log("Base64: " + base64EncodedImage);
    }
  }, []);

  return (
    <div>
      <Navv />
      <h4>Sell a product</h4>
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for="ProductName">Product Name</Label>
          <Input
            id="ProductName"
            name="pname"
            placeholder="Enter a cool name for your item here"
            type="text"
            value={formData.pname}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="initialPrice">Minimum Price</Label>
          <Input
            id="initialPrice"
            name="initialPrice"
            placeholder="There's no way I'm selling for less than this!"
            type="text"
            value={formData.initialPrice}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="Increment">Increment</Label>
          <Input
            id="Increment"
            name="increment"
            placeholder="What's the minimum by which you'd like a new bid to win?"
            type="number"
            value={formData.increment}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="Description">Description</Label>
          <Input
            id="Description"
            name="description"
            placeholder="Enter a cool name for your item here"
            type="text"
            value={formData.description}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="biddingTime">Bidding Time (in days)</Label>
          <Input
            id="biddingTime"
            name="biddingTime"
            placeholder="What's the minimum by which you'd like a new bid to win?"
            type="number"
            value={formData.biddingTime}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label>Upload Image of the product</Label>
          <Input
            type="file"
            name="file"
            onChange={(e) => handleFileInputChange(e)}
          />
        </FormGroup>
        <Button color="primary">Submit</Button>
      </Form>
      <Footer />
    </div>
  );
};

export default Sell;
