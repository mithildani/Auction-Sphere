import React from 'react'
import { Form, FormGroup, Label, Input} from 'reactstrap'
const Signup = () => {
  return (
    <div>Signup
      <Form>
      <FormGroup>
        <Label for="exampleEmail">
          Email
        </Label>
        <Input
          id="exampleEmail"
          name="email"
          placeholder="with a placeholder"
          type="email"
        />
      </FormGroup>
      <FormGroup>
        <Label for="examplePassword">
          Password
        </Label>
        <Input
          id="examplePassword"
          name="password"
          placeholder="password placeholder"
          type="password"
        />
        </FormGroup>
    </Form>
    </div>
  )
}

export default Signup