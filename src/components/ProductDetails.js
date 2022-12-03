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
import { URL } from '../global'
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
    
    console.log("first",now, endTime)
    const getProductDetails = async () => {
        try {
            let data = await axios.post(`${URL}/product/getDetails`, {
                productID: id,
            })
            console.log(data)
            setBids(data.data.bids)
            setProduct(data.data.product[0])
            setEndTime(data.data.product[0][7])
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
                            {product[1]}{' '}
                        </CardTitle>
                        <hr />
                        <CardImg
                            src={product[2]}
                            className="mx-auto"
                            style={{ width: '50%' }}
                        />
                        <CardText>
                            <p>Seller:&nbsp;&nbsp;{product[3]} </p>
                            <p>
                                Minimum price: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                                {product[4]}${' '}
                            </p>
                            <p>Date posted: &nbsp;&nbsp;&nbsp;{product[5]} </p>
                            <p>
                                Bidding window closes on: &nbsp;&nbsp;&nbsp;
                                {product[7]}{' '}
                            </p>
                            <p>
                                Minimum price increment to beat a bid:
                                &nbsp;&nbsp;&nbsp;
                                {product[6]}${' '}
                            </p>
                            <p>
                                Product Description: &nbsp;&nbsp;{product[8]}{' '}
                            </p>
                            {bids.length > 0 ? (
                                <>
                                    <h5>Current Highest bids:</h5>
                                    {bids.map((bid, index) => (
                                        <div key={index}>
                                            <p>
                                                Bidder: {bid[0] + ' ' + bid[1]}
                                            </p>
                                            <p>Bid amount: ${bid[2]}</p>
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
                                            sellerEmail={product[3]}
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
