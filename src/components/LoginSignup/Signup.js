import React, { useState } from 'react'
import {
    Form,
    FormGroup,
    Label,
    Input,
    Button,
    Card,
    CardBody,
    CardText,
    CardTitle,
    CardHeader,
} from 'reactstrap'
import { useNavigate } from 'react-router-dom'
import Navv from '../Navv'
import Footer from '../Footer'
import axios from 'axios'
import { URL } from '../../global'

/**
 * This component displays the Signup page of our application.
 */

const Signup = () => {
    const navigate = useNavigate()
    const handleChange = (event) => {
        setFormData({ ...formData, [event.target.name]: event.target.value })
    }
    const handleSubmit = async (event) => {
        event.preventDefault()
        if (formData.password !== formData.confirmPassword)
            alert('Passwords do not match')
        else {
            console.log(formData)
            try {
                let response = await axios.post(`${URL}/signup`, formData)
                console.log(response)
                navigate('/login')
                // alert("Form submitted successfully I think");
            } catch (e) {
                alert('Something went wrong')
                console.log(e)
            }
        }
    }
    const [formData, setFormData] = useState({
        firstName: '',
        lastName: '',
        contact: '',
        email: '',
        // address: "",
        password: '',
        confirmPassword: '',
    })
    return (
        <div>
            <Navv />
            {localStorage.getItem('auth') === 'true' ? (
                <></>
            ) : (
                <>
                    <Card body className="mx-auto" style={{ width: '60%' }}>
                        <CardHeader>
                            <h3>Sign up and bid away!</h3>
                        </CardHeader>
                        <CardBody>
                            <CardText>
                                <Form onSubmit={handleSubmit}>
                                    <FormGroup>
                                        <Label for="FirstName">
                                            First Name
                                        </Label>
                                        <Input
                                            id="FirstName"
                                            name="firstName"
                                            placeholder="Your good name, sir?"
                                            type="text"
                                            value={formData.firstName}
                                            onChange={(e) => handleChange(e)}
                                        />
                                    </FormGroup>
                                    <FormGroup>
                                        <Label for="LastName">Last Name</Label>
                                        <Input
                                            id="LastName"
                                            name="lastName"
                                            placeholder="Family name"
                                            type="text"
                                            value={formData.lastName}
                                            onChange={(e) => handleChange(e)}
                                        />
                                    </FormGroup>
                                    <FormGroup>
                                        <Label for="Contact">Contact</Label>
                                        <Input
                                            id="Contact"
                                            name="contact"
                                            placeholder="Just for our records, we're not asking you out *yet* :)"
                                            type="text"
                                            value={formData.contact}
                                            onChange={(e) => handleChange(e)}
                                        />
                                    </FormGroup>
                                    <FormGroup>
                                        <Label for="Email">Email</Label>
                                        <Input
                                            id="Email"
                                            name="email"
                                            placeholder="We solemnly swear we are up to no spamming :)"
                                            type="email"
                                            value={formData.email}
                                            onChange={(e) => handleChange(e)}
                                        />
                                    </FormGroup>
                                    {/* <FormGroup>
          <Label for="Address">Address</Label>
          <Input
            id="Address"
            name="address"
            placeholder="We promise to not come over, atleast not unannounced :)"
            type="textarea"
            value={formData.address}
            onChange={(e) => handleChange(e)}
          />
        </FormGroup> */}
                                    <FormGroup>
                                        <Label for="Password">Password</Label>
                                        <Input
                                            id="Password"
                                            name="password"
                                            placeholder="Type your crush's name here 👀"
                                            type="password"
                                            value={formData.password}
                                            onChange={(e) => handleChange(e)}
                                        />
                                    </FormGroup>
                                    <FormGroup>
                                        <Label for="ConfirmPassword">
                                            Confirm Password
                                        </Label>
                                        <Input
                                            id="ConfirmPassword"
                                            name="confirmPassword"
                                            placeholder="Confirm your crush ;)"
                                            type="password"
                                            value={formData.confirmPassword}
                                            onChange={(e) => handleChange(e)}
                                        />
                                    </FormGroup>
                                    <Button color="primary">Submit</Button>
                                </Form>
                            </CardText>
                        </CardBody>
                    </Card>

                    <br />
                </>
            )}
            <Footer />
        </div>
    )
}

export default Signup
