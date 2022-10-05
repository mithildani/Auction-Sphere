import React, { useState } from "react";
import { Form, FormGroup, Label, Input, Navbar, Button } from "reactstrap";
import axios from "axios";
import Navv from "../Navv";
import Footer from "../Footer";
import { URL } from "../../global";
import { useNavigate } from "react-router-dom";

/**
 * This component displays the Login Page
 */
const Login = () => {
  const handleChange = (event) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };
  const navigate = useNavigate();
  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(formData);
    let response;
    try {
      response = await axios.post(`${URL}/login`, formData);
      console.log(response);
      alert("Login success!");
      // Set local storage
      if (response.data.message === "Logged in successfully") {
        localStorage.setItem("auth", "true");
        localStorage.setItem("email", formData.email);
        navigate("/products");
      }
    } catch (e) {
      alert("Something went wrong");
      console.log(e);
    }
  };
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  return (
    <div>
      <Navv />
      <Form onSubmit={handleSubmit}>
        <FormGroup>
          <Label for="Email">Email</Label>
          <Input
            id="Email"
            name="email"
            placeholder="The email you registered with us"
            type="email"
            value={formData.email}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="Password">Password</Label>
          <Input
            id="Password"
            name="password"
            placeholder="Your password"
            type="password"
            value={formData.password}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup>
        <Button color="primary">Submit</Button>
      </Form>
      <div style={{ marginTop: "25rem", marginRight: "2rem" }}>
        <Footer />
      </div>
    </div>
  );
};

export default Login;
