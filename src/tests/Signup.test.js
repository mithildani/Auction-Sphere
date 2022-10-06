import { render, screen } from "@testing-library/react";
import Signup from "../components/LoginSignup/Signup";

const fields = [
  "First Name",
  "Last Name",
  "Contact",
  "Email",
  "Passsword",
  "Confirm Password",
];
test.each(fields)("Rendering the signup form", (field) => {
  render(<Signup />);
  const label = screen.getByText(field);
  expect(label).toBeInTheDocument();
});
