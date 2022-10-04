import React from "react";

const ProductCard = ({ product }) => {
  return (
    <>
      <span>
        id = {product.id}, name = {product.name}
      </span>
      <br />
    </>
  );
};

export default ProductCard;
