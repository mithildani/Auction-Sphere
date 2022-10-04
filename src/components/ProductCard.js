import React from "react";
import { Card, CardImg, CardBody, CardTitle, CardText } from "reactstrap";

const ProductCard = ({ product }) => {
  return (
    <>
      <Card className="my-2" style={{ width: "70%" }}>
        <CardImg
          alt="Card image cap"
          src="https://picsum.photos/900/180"
          style={{
            height: 180,
            width: 500,
          }}
          width="50%"
        />
        <CardBody>
          <CardTitle tag="h5">Product Name = {product.name}</CardTitle>
          <CardText>Product description = {product.description}</CardText>
          <CardText>
            <small className="text-muted">id = {product.id}</small>
          </CardText>
        </CardBody>
      </Card>
    </>
  );
};

export default ProductCard;
