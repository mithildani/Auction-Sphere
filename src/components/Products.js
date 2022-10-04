import React from "react";
import Footer from "./Footer";
import Navv from "./Navv";
import ProductCard from "./ProductCard";

const Products = () => {
  let products = [
    { id: 1, name: "prod1" },
    { id: 2, name: "prod2" },
  ];
  return (
    <>
      <Navv />
      {products.map((product) => (
        <ProductCard product={product} />
      ))}
      <Footer />
    </>
  );
};

export default Products;
