import React, { useState } from "react";
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
} from "reactstrap";
import logo from "../assets/NavLogo.png";

function Navv(args) {
  const [isOpen, setIsOpen] = useState(true);

  const toggle = () => setIsOpen(!isOpen);

  return (
    <div>
      <Navbar style={{ marginBottom: "1rem" }} color="light" light expand="md">
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
            setIsOpen(!isOpen);
          }}
        />

        <Collapse isOpen={isOpen} navbar>
          <Nav className="mr-auto" navbar>
            <NavItem>
              <NavLink href="/products">Products</NavLink>
            </NavItem>
            {/* {localStorage.getItem('auth') === 'true' ? (<></>) : (
              <>
              <NavItem>
              <NavLink href="/login">Login</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/">Signup</NavLink>
            </NavItem>
              </>
            )} */}
            <NavItem>
              <NavLink href="/login">Login</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/">Signup</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/sell">Sell</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}

export default Navv;
