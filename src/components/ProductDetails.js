import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import {
    Button,
    Card,
    CardImg,
    CardBody,
    CardTitle,
    CardText,
    Row,
    Col,
    CardHeader,
    CardGroup,
    CardSubtitle,
} from 'reactstrap'
import axios from 'axios'
import moment from 'moment'

import AddBid from './AddBid'
import Footer from './Footer'
import Navv from './Navv'
import { ProductMS_BaseURL } from '../global'
import { toast } from 'react-toastify'
import Timer from './Timer'

/**
 * This component is the details page of a single product.
 */

const ProductDetails = () => {
    let { id } = useParams()
    const [showAddBid, setShowAddBid] = useState(false)
    const [showButton, setShowButton] = useState(false)
    const [bids, setBids] = useState([])
    const [product, setProduct] = useState(null)
    const [endTime, setEndTime] = useState()
    const now = moment()
    
    const getProductDetails = async () => {
        try {
            let data = await axios.post(`${ProductMS_BaseURL}/product/getDetails`, {
                productID: id,
            })
            console.log(data)
            setBids(data.data.bids)
            setProduct(data.data.product[0])
            setEndTime(data.data.product[0].deadline_date)
        } catch (error) {
            toast.error('Something went wrong')
        }
    }
    useEffect(() => {
        getProductDetails()
        if (typeof window !== 'undefined') {
            if (localStorage.getItem('auth') === 'true') {
                setShowButton(true)
            }
        }
    }, [])
    return (
        <>
            <Navv />
            <Card
                className="mx-auto"
                color="light"
                outline
                style={{
                    width: '45rem',
                    textAlign: 'center',
                }}
            >
                {product && (
                    <div>
                        <Timer time={endTime}/>
                        <CardTitle tag="h3" style={{ textAlign: 'center' }}>
                            {product.name}{' '}
                        </CardTitle>
                        <hr />
                        <CardImg
                            src={product.photo}
                            className="mx-auto"
                            style={{ width: '50%' }}
                        />
                        <CardText>
                            <p>Seller:&nbsp;&nbsp;{product.email} </p>
                            <p>
                                Minimum price: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                {product.initial_price}${' '}
                            </p>
                            <p>Date posted: &nbsp;&nbsp;&nbsp;{product.date} </p>
                            <p>
                                Bidding window closes on: &nbsp;&nbsp;&nbsp;
                                {product.deadline_date}{' '}
                            </p>
                            <p>
                                Minimum price increment to beat a bid:
                                &nbsp;&nbsp;&nbsp;
                                {product.increment}${' '}
                            </p>
                            <p>
                                Product Description: &nbsp;&nbsp;{product.description}{' '}
                            </p>
                            {bids.length > 0 ? (
                                <>
                                    <h5>Current Highest bids:</h5>
                                    {bids.map((bid, index) => (
                                        <div key={index}>
                                            <p>
                                                Bidder: {bid.first_name + ' ' + bid.last_name}
                                            </p>
                                            <p>Bid amount: ${bid.bid_amount}</p>
                                        </div>
                                    ))}
                                </>
                            ) : (
                                <h5>No bids so far</h5>
                            )}
                            {showButton && (
                                <>
                                    <Button
                                        color="info"
                                        onClick={() =>
                                            setShowAddBid(!showAddBid)
                                        }
                                        disabled={endTime>now}
                                    >
                                        {showAddBid ? (
                                            <span>-</span>
                                        ) : (
                                            <span>+</span>
                                        )}{' '}
                                        Add a Bid
                                    </Button>
                                    {showAddBid && (
                                        <AddBid
                                            productId={id}
                                            sellerId={product.seller_id}
                                        />
                                    )}
                                </>
                            )}
                        </CardText>
                    </div>
                )}
            </Card>
            <Footer />
        </>
    )
}

export default ProductDetails
