import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import {
    Card,
    CardImg,
    CardBody,
    CardTitle,
    CardText,
    Button,
} from 'reactstrap'
import PropTypes from 'prop-types'

/**
 * This component displays a single product card on the products page.
 */

const ProductCard = ({ product, maxBid, name }) => {
    const [url, setUrl] = useState(`/details/${product[0]}`)

    return (
        <>
            <Card className="my-2" style={{ width: '70%' }}>
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
                    <CardTitle tag="h5">{product[1]}</CardTitle>
                    <CardText>Seller: {product[2]}</CardText>
                    {/* <CardText>Description: {product[7]}</CardText> */}
                    <CardText>Minimum price: ${product[3]}</CardText>
                    <CardText>Current highest bids: ${maxBid}</CardText>
                    <CardText>Current highest bidder: {name}</CardText>
                    {/* <CardText>
            <small className="text-muted">id = {product[0]}</small>
          </CardText> */}
                </CardBody>
                <Button
                    color="warning"
                    href={url}
                    style={{
                        width: '15%',
                        marginLeft: '0.5rem',
                        marginBottom: '0.5rem',
                    }}
                >
                    Details
                </Button>
            </Card>
        </>
    )
}

ProductCard.propTypes = {
    product: PropTypes.array.isRequired,
    maxBid: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
}

export default ProductCard
