from unittest import mock
from unittest.mock import patch, MagicMock, Mock

import app


def test_hello_world():
    assert (app.hello_world() == "<p>Hello, World!</p>")


@patch('app.create_connection')
def test_get_product_image(mock_create_call):
    mock_create_call = MagicMock()
    connection = Mock()
    cursor = connection.cursor()
    mock_create_call.return_value = connection
    m = mock.MagicMock()
    m.values = {"productID": "1"}
    with mock.patch("app.request", m):
        result = app.get_product_image()
        # print("result=", result)
    assert m.values.keys().__contains__("productID")
