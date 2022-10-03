import React from 'react'
import { Form, FormGroup, Label, Input, Navbar} from 'reactstrap'
import Navv from './Navv'
const Login = () => {
  return (
    <div>
        <Navv />
      <Form>
      <FormGroup>
        <Label for="Email">
          Email
        </Label>
        <Input
          id="Email"
          name="email"
          placeholder="Enter your registered email here"
          type="email"
        />
      </FormGroup>
      <FormGroup>
        <Label for="Password">
          Password
        </Label>
        <Input
          id="Password"
          name="password"
          placeholder="password placeholder"
          type="password"
        />
        </FormGroup>
    </Form>
    </div>
  )
}

export default Login