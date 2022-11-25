import React, { useEffect, useState } from 'react'
import Footer from './Footer'
import Navv from './Navv'
import ProductCard from './ProductCard'
import Pagination from './Pagination'
import { URL } from '../global'
import axios from 'axios'
import { CardGroup, Row } from 'reactstrap'
import { toast } from 'react-toastify'

/**
 * This component displays all products on the products page.
 */

const Products = () => {
    const [apiData, setApiData] = useState([])
    const [currentPage, setCurrentPage] = useState(1);
    let PageSize = 10; //default page size = 10
    const [totalCount, setTotalCount] = useState(0);

    const getProducts = async (page) => {
        try {
            let data = await axios.get(`${URL}/getLatestProducts?pageSize=${PageSize}&pageNum=${page}`)
            setApiData(data.data)
            setTotalCount(data.data.total)
        } catch (error) {
            toast.error('Something went wrong')
            console.log(error)
        }
    }
    useEffect(() => {
        getProducts(currentPage)
    }, [currentPage])
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
            <Pagination
                className="pagination-bar"
                currentPage={currentPage}
                totalCount={totalCount}
                pageSize={PageSize}
                onPageChange={page => { setCurrentPage(page); getProducts(page); } }
            />
            <Footer />
        </>
    )
}

export default Products
