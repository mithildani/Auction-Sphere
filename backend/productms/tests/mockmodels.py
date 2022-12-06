import pytest

from models import Users, Product, Bids
from app import app

@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy.model._QueryProperty.__get__").return_value = mocker.Mock()
    return mock

@pytest.fixture()
def request_context():

    # other setup can go here
    return app.test_request_context

    # clean up / reset resources here


@pytest.fixture
def mock_my_model():
    my_model = Product(
        prod_id = 1,
        name = "Gun",
        photo = "https://ibb.co/7SpZhTs",
        seller_id = 1,
        initial_price = 10,
        date = "2022-12-01",
        increment = 2,
        deadline_date = "2022-12-07",
        description = "Good quality Nerf Guns",
        email_sent = False
    )
    return my_model

@pytest.fixture
def mock_product_1():
    my_model = Product(
        prod_id = 1,
        name = "Gun",
        photo = "https://ibb.co/7SpZhTs",
        seller_id = 1,
        initial_price = 10,
        date = "2022-12-01",
        increment = 2,
        deadline_date = "2022-12-07",
        description = "Good quality Nerf Guns",
        email_sent = False
    )
    return my_model

@pytest.fixture
def mock_product_user_1():
    return {
        "prod_id": 1,
        "name": "Gun",
        "photo": "https://ibb.co/7SpZhTs",
        "seller_id": 1,
        "initial_price": 10,
        "date": "2022-12-01",
        "increment": 2,
        "deadline_date": "2022-12-07",
        "description": "Good quality Nerf Guns",
        "email": "danimithil@gmail.com"
    }

@pytest.fixture
def mock_product_user_2():
    return {
        "prod_id": 2,
        "name": "Bullet",
        "photo": "https://ibb.co/7SpZhTs",
        "seller_id": 1,
        "initial_price": 15,
        "date": "2022-12-01",
        "increment": 2,
        "deadline_date": "2022-12-07",
        "description": "Good quality Nerf Guns",
        "email": "danimithil@gmail.com"
    }

@pytest.fixture
def mock_product_user_3():
    return {
        "prod_id": 3,
        "name": "Car",
        "photo": "https://ibb.co/7SpZhTs",
        "seller_id": 1,
        "initial_price": 1000,
        "date": "2022-12-01",
        "increment": 50,
        "deadline_date": "2022-12-07",
        "description": "Good quality Nerf Cars",
        "email": "danimithil@gmail.com"
    }

@pytest.fixture
def mock_bid_1():
    return {
        "first_name": "Mithil",
        "last_name": "Dani",
        "bid_amount": 20.0
    }

@pytest.fixture
def mock_bid_2():
    return {
        "first_name": "Vansh",
        "last_name": "Mehta",
        "bid_amount": 15.0
    }

@pytest.fixture
def mock_bid_3():
    return {
        "first_name": "Neha",
        "last_name": "Kale",
        "bid_amount": 12.0
    }

@pytest.fixture
def mock_obj_bid_1(mocker):
    bid = mocker.Mock()
    bid.bid_amount = 20.0
    bid.user.first_name = "Mithil"
    
@pytest.fixture
def mock_obj_bid_2(mocker):
    bid = mocker.Mock()
    bid.bid_amount = 15.0
    bid.user.first_name = "Vansh"
    
@pytest.fixture
def mock_obj_bid_3(mocker):
    bid = mocker.Mock()
    bid.bid_amount = 12.0
    bid.user.first_name = "Neha"