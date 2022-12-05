from unittest.mock import PropertyMock
import app
from app import get_product_image
from tests.mockmodels import mock_get_sqlalchemy, request_context
import flask


def test_get_image(
    mock_get_sqlalchemy,
    mocker,
    request_context
):

    with request_context():
        # Mocking request
        request_mock = mocker.patch('app.request')
        
    # Mocking Cache Call
    photo_cache_mock = mocker.patch("app.ProductCache")
    photo_cache_mock().get_configuration.return_value = None
    photo_cache_mock().photo = "https://ibb.co/7SpZhTs"

    # test function
    response = get_product_image()

    # expectation
    expected_response = {"result": "https://ibb.co/7SpZhTs"}

    assert response == expected_response