import { render, screen } from "@testing-library/react";
import Footer from "../components/Footer";

test("renders  Footer", () => {
  render(<Footer />);
  const footer_content = screen.getByText(
    "One stop portal for auctioning and selling items. Created by Tanvi Sinha, Kartik Soni, Palash Rathod, Shreya Maheshwari, and Nandini Mundra. Improved by Neha Kale, Rishikesh Yelne, Mithil Dani, Vansh Mehta and Ritwik Vaidya :)"
  );
  expect(footer_content).toBeInTheDocument();
});
