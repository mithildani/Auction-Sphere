import { render, screen } from "@testing-library/react";
import Navv from "../components/Navv";

const tabs = [
  { text: "Signup", location: "/signup" },
  { text: "Login", location: "/login" },
  { text: "Products", location: "/products" },
];
test("renders Nav bar", () => {
  render(<Navv />);
  const linkElement = screen.getByText(/Products/i);
  expect(linkElement).toBeInTheDocument();
});

test.each(tabs)("Each tab working", (tab) => {
  render(<Navv />);
  const tab_link = screen.getByText(tab.text);
  expect(tab_link).toHaveAttribute("href", tab.location);
});
