import pytest

from userms.app import app
from userms.models import Users


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
    my_model = Users(
        first_name="Sam",
        last_name="Mason",
        email="sam.mason@gmail.com",
        contact_number="1234567890",
        password="1234"
    )

    return my_model


@pytest.fixture
def mock_user_1():
    my_model = Users(
        first_name="Dam",
        last_name="Krason",
        email="dam.krason@gmail.com",
        contact_number="1234567890",
        password="1234"
    )

    return my_model


@pytest.fixture
def mock_user_2():
    my_model = Users(
        first_name="Ram",
        last_name="Vason",
        email="ram.vason@gmail.com",
        contact_number="1234567890",
        password="1234"
    )

    return my_model
