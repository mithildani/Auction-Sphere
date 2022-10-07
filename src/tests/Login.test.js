import { render, screen } from "@testing-library/react";
import Login from "../components/LoginSignup/Login.js";
import { BrowserRouter as Router } from "react-router-dom";
const fields = [
  { field_label: "Email", node_name: "email" },
  { field_label: "Password", node_name: "password" },
];
test.each(fields)("Rendering the login form", (field) => {
  render(
    <Router>
      <Login />
    </Router>
  );
  const label = screen.getByText(field.field_label);
  expect(label).toBeInTheDocument();
});

test.each(fields)("Fields have labels", (field) => {
  render(
    <Router>
      <Login />
    </Router>
  );
  const inputNode = screen.getByLabelText(field.field_label);
  expect(inputNode.getAttribute("name")).toBe(field.node_name);
});
