import "./App.css";
// import { Routes ,Route } from 'react-router-dom';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Signup from "./components/LoginSignup/Signup";
import Login from "./components/LoginSignup/Login";
import Products from "./components/Products";
import Sell from "./components/Sell";
import ProductDetails from "./components/ProductDetails";
import AddBid from "./components/AddBid";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Signup />}>
          {/* <Route index element={<Signup />} /> */}
        </Route>
        <Route path="/login" element={<Login />} />
        <Route path="/products" element={<Products />} />
        <Route path="/sell" element={<Sell />} />
        <Route path="/details/:id" element={<ProductDetails />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
