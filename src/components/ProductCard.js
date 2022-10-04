import React, { useState } from "react";
import { Link } from "react-router-dom";
import {
  Card,
  CardImg,
  CardBody,
  CardTitle,
  CardText,
  Button,
} from "reactstrap";

const ProductCard = ({ product }) => {
  const [url, setUrl] = useState(`/details/${product.id}`);

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
        <Button
          color="warning"
          href={url}
          style={{
            width: "15%",
            marginLeft: "0.5rem",
            marginBottom: "0.5rem",
          }}
        >
          Details
        </Button>
      </Card>
    </>
  );
};

export default ProductCard;
