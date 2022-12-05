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