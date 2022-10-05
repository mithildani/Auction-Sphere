import React, { useEffect, useState } from "react";
import Footer from "./Footer";
import Navv from "./Navv";
import ProductCard from "./ProductCard";
import { URL } from "../global";
import axios from "axios";

const Products = () => {
  const [allProducts, setAllProducts] = useState([]);
  let products = [
    { id: 1, name: "prod1", description: "jhadsbfusjkan fksdufj,nsajfkjdsa" },
    { id: 2, name: "prod2", description: "jhadsbfusjkan fksdufj,nsajfkjdsa" },
  ];
  const getProducts = async () => {
    let data = await axios.get(`${URL}/getLatestProducts`);
    console.log(data);
  };
  useEffect(() => {
    getProducts();
  }, []);

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
