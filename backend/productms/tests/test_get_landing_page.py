from app import get_landing_page
from tests.mockmodels import request_context, mock_get_sqlalchemy, \
    mock_product_user_1, mock_product_user_2, mock_product_user_3, \
    mock_obj_bid_1, mock_obj_bid_2, mock_obj_bid_3


def test_get_landing_page_0_products_0_bid(
    mocker, request_context, 
    mock_get_sqlalchemy,
):

    with request_context():
        # Mocking request
        request_mock = mocker.patch('app.request')
        
    # Mocking DB Calls
    mock_get_sqlalchemy.join.return_value \
        .with_entities.return_value \
        .order_by.return_value \
        .limit.return_value \
        .offset.return_value = []
    
    mock_get_sqlalchemy.count.return_value=0

    mock_get_sqlalchemy.join.return_value \
        .filter.return_value \
        .order_by.return_value \
        .limit.return_value \
        .first.return_value = None

    # test function
    response = get_landing_page()

    # expectation
    expected_response = response = {
        "products": [], 
        "maximumBids": [],
        "names": [], 
        "total": 0
    }

    assert response == expected_response

def test_get_landing_page_3_products_0_bid(
    mocker, request_context, 
    mock_get_sqlalchemy,
    mock_product_user_1, 
    mock_product_user_2, 
    mock_product_user_3, 
):

    with request_context():
        # Mocking request
        request_mock = mocker.patch('app.request')
        
    # Mocking DB Calls
    mock_get_sqlalchemy.join.return_value \
        .with_entities.return_value \
        .order_by.return_value \
        .limit.return_value \
        .offset.return_value = [mock_product_user_1, mock_product_user_2, mock_product_user_3]
    
    mock_get_sqlalchemy.count.return_value=3

    mock_get_sqlalchemy.join.return_value \
        .filter.return_value \
        .order_by.return_value \
        .limit.return_value \
        .first.return_value = None

    # test function
    response = get_landing_page()

    # expectation
    expected_response = response = {
        "products": [mock_product_user_1, mock_product_user_2, mock_product_user_3], 
        "maximumBids": [-1, -1, -1],
        "names": ["N/A", "N/A", "N/A"], 
        "total": 3
    }

    assert response == expected_response

def test_get_landing_page_3_product_3_bids(
    mocker, request_context, mock_get_sqlalchemy,
    mock_product_user_1, 
    mock_product_user_2, 
    mock_product_user_3, 
    mock_obj_bid_1, mock_obj_bid_2, mock_obj_bid_3
):

    with request_context():
        # Mocking request
        request_mock = mocker.patch('app.request')
        
    # Mocking DB Calls
    mock_get_sqlalchemy.join.return_value \
        .with_entities.return_value \
        .order_by.return_value \
        .limit.return_value \
        .offset.return_value = [mock_product_user_1, mock_product_user_2, mock_product_user_3]
    
    mock_get_sqlalchemy.count.return_value=3

    bids = [mock_obj_bid_1, mock_obj_bid_2, mock_obj_bid_3]
    mock_get_sqlalchemy.join.return_value \
        .filter.return_value \
        .order_by.return_value \
        .limit.return_value \
        .first.return_value = bids[ mock_get_sqlalchemy.join.return_value \
                                    .filter.return_value \
                                    .order_by.return_value \
                                    .limit.return_value \
                                    .first.return_value.call_count-1]

    # test function
    response = get_landing_page()

    # expectation
    expected_response = response = {
        "products": [mock_product_user_1, mock_product_user_2, mock_product_user_3], 
        "maximumBids": [20.0, 15.0, 12.0],
        "names": ["Mithil", "Vansh", "Neha"], 
        "total": 3
    }

    assert response == expected_response