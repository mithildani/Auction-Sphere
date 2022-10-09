import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { Button } from 'reactstrap'
import axios from 'axios'

import AddBid from './AddBid'
import Footer from './Footer'
import Navv from './Navv'
import { URL } from '../global'

/**
 * This component is the details page of a single product.
 */

const ProductDetails = () => {
    let { id } = useParams()
    const [showAddBid, setShowAddBid] = useState(false)
    const [showButton, setShowButton] = useState(false)
    const [bids, setBids] = useState([])
    const [product, setProduct] = useState(null)
    const getProductDetails = async () => {
        try {
            let data = await axios.post(`${URL}/product/getDetails`, {
                productID: id,
            })
            console.log(data)
            setBids(data.data.bids)
            setProduct(data.data.product[0])
        } catch (error) {
            alert('Something went wrong')
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

            {/* <h5>Product details:</h5> */}
            {product && (
                <div>
                    {/* <p>Product ID: {product[0]} </p> */}
                    <h2>{product[1]} </h2>
                    {/* <p>Image: {product[2]} </p> */}
                    <img
                        src={product[2]}
                        style={{
                            marginBottom: '2rem',
                            width: '20%',
                            height: '20%',
                        }}
                    ></img>
                    <p>Seller: {product[3]} </p>
                    <p>Minimum price {product[4]} </p>
                    <p>Date posted: {product[5]} </p>
                    <p>Bidding window closes on: {product[7]} </p>
                    <p>Minimum price increment to beat a bid: {product[6]} </p>
                    <p>Product Description: {product[8]} </p>
                </div>
            )}
            {bids.length > 0 ? (
                <>
                    <h5>Current Highest bids:</h5>
                    {bids.map((bid, index) => (
                        <div key={index}>
                            <p>Bidder: {bid[0] + ' ' + bid[1]}</p>
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
                        onClick={() => setShowAddBid(!showAddBid)}
                    >
                        {showAddBid ? <span>-</span> : <span>+</span>} Add a Bid
                    </Button>
                    {showAddBid && (
                        <AddBid productId={id} sellerEmail={product[3]} />
                    )}
                </>
            )}
            {/* <Footer /> */}
        </>
    )
}

export default ProductDetails
