import React, { useState } from 'react'
import { toast } from 'react-toastify'
import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    UncontrolledDropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem,
    NavbarText,
} from 'reactstrap'
import logo from '../assets/NavLogo.png'

/**
 * This component is the Navigation bar of our application.
 */

function Navv(args) {
    const [isOpen, setIsOpen] = useState(true)

    const toggle = () => setIsOpen(!isOpen)
    const handleLogout = () => {
        localStorage.clear()
        window.location.reload()
        toast.info('Logged out')
    }

    return (
        <div>
            <Navbar
                style={{ marginBottom: '1rem' }}
                color="light"
                light
                expand="md"
            >
                <NavbarBrand href="/">
                    <img
                        src={logo}
                        style={{
                            height: 40,
                            width: 60,
                        }}
                    />
                </NavbarBrand>
                <NavbarToggler
                    onClick={() => {
                        setIsOpen(!isOpen)
                    }}
                />

                <Collapse isOpen={isOpen} navbar>
                    <Nav className="justify-content-end" navbar>
                        <NavItem>
                            <NavLink href="/products">Products</NavLink>
                        </NavItem>
                        {localStorage.getItem('auth') === 'true' ? (
                            <>
                                <NavItem>
                                    <NavLink href="/sell">Sell</NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink href="/" onClick={handleLogout}>
                                        Logout
                                    </NavLink>
                                </NavItem>
                            </>
                        ) : (
                            <>
                                <NavItem className="float-right">
                                    <NavLink href="/login">Login</NavLink>
                                </NavItem>
                                <NavItem>
                                    <NavLink href="/signup">Signup</NavLink>
                                </NavItem>
                            </>
                        )}
                    </Nav>
                </Collapse>
            </Navbar>
        </div>
    )
}

export default Navv
