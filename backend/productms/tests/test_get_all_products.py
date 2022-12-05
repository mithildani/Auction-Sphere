from app import get_all_products
from tests.mockmodels import mock_get_sqlalchemy, mock_product_1


def test_0_product(
    mock_get_sqlalchemy,
    mocker,
):

    # mocking db call
    mock_get_sqlalchemy.order_by.return_value.all.return_value = []

    # test function
    response = get_all_products()
    print(response)
    # expectation
    expected_response = {
        "result": []        
    }

    assert response == expected_response
    

def test_1_product(
    mock_get_sqlalchemy,
    mocker,
    mock_product_1
):

    # mocking db call
    mock_get_sqlalchemy.order_by.return_value.all.return_value = [mock_product_1]

    # test function
    response = get_all_products()
    print(response)
    # expectation
    expected_response = {
        "result": [{
            "prod_id": 1,
            "name": "Gun",
            "photo": "https://ibb.co/7SpZhTs",
            "seller_id": 1,
            "initial_price": 10,
            "date": "2022-12-01",
            "increment": 2,
            "deadline_date": "2022-12-07",
            "description": "Good quality Nerf Guns",
        }]        
    }

    assert response == expected_response

