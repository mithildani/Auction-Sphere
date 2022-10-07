import React from 'react'

/**
 * This component displays the Footer of our application.
 */

const Footer = () => {
    return (
        <div
            style={{
                position: 'fixed',
                bottom: '0',
                width: '100%',
                height: '9%',
                backgroundColor: '#F4F6F6 ',
            }}
            className="footer"
        >
            <div className="container">
                <div className="row">
                    <hr />
                    <p>
                        One stop portal for auctioning and selling items.
                        Created by Tanvi Sinha, Kartik Soni, Palash Rathod,
                        Shreya Maheshwari, and Nandini Mundra.
                    </p>
                </div>
            </div>
        </div>
    )
}

export default Footer
