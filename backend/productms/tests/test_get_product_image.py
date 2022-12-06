from app import get_product_image
from tests.mockmodels import request_context


def test_get_image(
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