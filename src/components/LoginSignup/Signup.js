import React from "react";
import { Form, FormGroup, Label, Input } from "reactstrap";
import About from "../About";
import Navv from "../Navv";
const Signup = () => {
  return (
    <div>
      <Navv />
      Signup
      <Form>
        <FormGroup>
          <Label for="exampleEmail">Email</Label>
          <Input
            id="exampleEmail"
            name="email"
            placeholder="with a placeholder"
            type="email"
          />
        </FormGroup>
        <FormGroup>
          <Label for="examplePassword">Password</Label>
          <Input
            id="examplePassword"
            name="password"
            placeholder="password placeholder"
            type="password"
          />
        </FormGroup>
      </Form>
      <br />
      <div style={{ marginLeft: "1rem" }}>
        <About />
      </div>
    </div>
  );
};

export default Signup;
