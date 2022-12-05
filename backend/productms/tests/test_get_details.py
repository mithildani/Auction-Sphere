from app import get_product_details
from tests.mockmodels import request_context, mock_get_sqlalchemy, mock_product_user_1, mock_bid_1, mock_bid_2, mock_bid_3

def test_get_product_detail_0_bids(
    mocker, request_context, 
    mock_get_sqlalchemy,
    mock_product_user_1, 
):

    with request_context():
        # Mocking request
        request_mock = mocker.patch('app.request')
        
    # Mocking DB Calls
    mock_get_sqlalchemy.join.return_value \
        .with_entities.return_value \
        .filter_by.return_value.all.return_value = [mock_product_user_1]

    mock_get_sqlalchemy.join.return_value. \
        with_entities.return_value. \
        filter.return_value. \
        order_by.return_value = []

    # test function
    response = get_product_details()

    # expectation
    expected_response = {
        "product": [
            mock_product_user_1
        ],
        "bids": []
    }

    assert response == expected_response

def test_get_product_detail_3_bids(
    mocker, request_context, mock_get_sqlalchemy,
    mock_product_user_1, mock_bid_1, mock_bid_2, mock_bid_3
):

    with request_context():
        # Mocking request
        request_mock = mocker.patch('app.request')
        
    # Mocking DB Calls
    mock_get_sqlalchemy.join.return_value \
        .with_entities.return_value \
        .filter_by.return_value.all.return_value = [mock_product_user_1]

    mock_get_sqlalchemy.join.return_value. \
        with_entities.return_value. \
        filter.return_value. \
        order_by.return_value = [mock_bid_1, mock_bid_2, mock_bid_3]

    # test function
    response = get_product_details()

    # expectation
    expected_response = {
        "product": [
            mock_product_user_1
        ],
        "bids": [
            mock_bid_1,
            mock_bid_2,
            mock_bid_3,
        ]
    }

    assert response == expected_response