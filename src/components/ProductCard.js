import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import {
    Card,
    CardImg,
    CardBody,
    CardTitle,
    CardText,
    Button,
    Row,
    Col,
    CardHeader,
    CardGroup,
    CardSubtitle,
} from 'reactstrap'
import PropTypes from 'prop-types'
import axios from 'axios'
import { ProductMS_BaseURL } from '../global'
import '../css/card.css'
import { toast } from 'react-toastify'

/**
 * This component displays a single product card on the products page.
 */

const ProductCard = ({ product, maxBid, name }) => {
    const [url, setUrl] = useState(`/details/${product.prod_id}`)
    const [image, setImage] = useState('https://picsum.photos/900/180')
    
    const fetchImage = async () => {
        try {
            console.log(product);
            const response = await axios.post(`${ProductMS_BaseURL}/product/getImage`, {
                productID: product.prod_id,
            })
            console.log(response);
            setImage(response.data.result)
        } catch (e) {
            toast.error(e)
        }
    }
    useEffect(() => {
        fetchImage()
    }, [product])

    return (
        <>
            <Card class="card">
                <CardTitle tag="h3" style={{ textAlign: 'center' }}>
                    {product.name}
                </CardTitle>
                <hr />
                <CardImg
                    className="mx-auto"
                    src={image}
                    style={{ width: '50%', textAlign: 'center' }}
                />
                {/* <img alt="Sample" src={image} /> */}
                <CardBody>
                    <CardText>Seller: {product.email}</CardText>
                    <CardText>Minimum price: ${product.initial_price}</CardText>
                    <CardText>
                        Current highest bids: ${maxBid === -1 ? 'N/A' : maxBid}
                    </CardText>
                    <CardText>Current highest bidder: {name}</CardText>
                    <Button color="warning" href={url}>
                        Details
                    </Button>
                </CardBody>
            </Card>

            {/* <Card className="my-2" style={{ width: '70%' }}>
                <CardImg
                    alt="Card image cap"
                    src={image}
                    style={{
                        height: 180,
                        width: 500,
                    }}
                    width="50%"
                />
                <CardBody>
                    <CardTitle tag="h5">{product[1]}</CardTitle>
                    <CardText>Seller: {product[2]}</CardText>
                    <CardText>Minimum price: ${product[3]}</CardText>
                    <CardText>
                        Current highest bids: ${maxBid === -1 ? 'N/A' : maxBid}
                    </CardText>
                    <CardText>Current highest bidder: {name}</CardText>
                </CardBody>
            </Card> */}
        </>
    )
}

ProductCard.propTypes = {
    product: PropTypes.array.isRequired,
    maxBid: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
}

export default ProductCard
