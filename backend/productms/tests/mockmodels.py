import pytest

from models import Users, Product, Bids


@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy.model._QueryProperty.__get__").return_value = mocker.Mock()
    return mock


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