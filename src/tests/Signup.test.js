import { render, screen } from "@testing-library/react";
import Signup from "../components/LoginSignup/Signup.js";

const fields = [
  { field_label: "First Name", node_name: "firstName" },
  { field_label: "Last Name", node_name: "lastName" },
  { field_label: "Contact", node_name: "contact" },
  { field_label: "Email", node_name: "email" },
  { field_label: "Passsword", node_name: "password" },
  { field_label: "Confirm Password", node_name: "confirmPassword" },
];
test.each(fields)("Rendering the signup form", (field) => {
  render(<Signup />);
  const label = screen.getByText(field.field_label);
  expect(label).toBeInTheDocument();
});

test.each(fields)("Fields have labels", (field) => {
  render(<Signup />);
  const inputNode = screen.getByLabelText(field.field_label);
  expect(inputNode.getAttribute("name")).toBe(field.node_name);
});
