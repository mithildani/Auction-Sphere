import React, { useEffect, useState } from 'react'
import Footer from './Footer'
import Navv from './Navv'
import ProductCard from './ProductCard'
import { URL } from '../global'
import axios from 'axios'
import { CardGroup, Row } from 'reactstrap'

/**
 * This component displays all products on the products page.
 */

const Products = () => {
    const [apiData, setApiData] = useState([])

    const getProducts = async () => {
        try {
            let data = await axios.get(`${URL}/getLatestProducts`)
            console.log(data.data)
            setApiData(data.data)
        } catch (error) {
            alert('Something went wrong')
            console.log(error)
        }
    }
    useEffect(() => {
        getProducts()
    }, [])

    return (
        <>
            <Navv />
            {/* {products.map((product) => (
        <ProductCard product={product} />
      ))} */}
            <Row>
                {apiData && apiData.products ? (
                    apiData.products.map((product, index) => (
                        <ProductCard
                            key={index}
                            product={product}
                            maxBid={apiData.maximumBids[index]}
                            name={apiData.names[index]}
                        />
                    ))
                ) : (
                    <div>No products found</div>
                )}
            </Row>
            <Footer />
        </>
    )
}

export default Products
