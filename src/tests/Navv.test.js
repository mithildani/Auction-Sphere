import { render, screen } from "@testing-library/react";
import Navv from "../components/Navv";

test("renders Nav bar", () => {
  render(<Navv />);
  const linkElement = screen.getByText(/Products/i);
  expect(linkElement).toBeInTheDocument();
});
