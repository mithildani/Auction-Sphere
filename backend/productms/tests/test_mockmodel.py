from models import Product
from tests.mockmodels import mock_my_model, mock_get_sqlalchemy


def test_sqlalchemy_query_property_get_mock(
        mock_my_model,
        mock_get_sqlalchemy,
):
    mock_get_sqlalchemy.order_by.return_value.all.return_value = [mock_my_model]
    response = Product.query.order_by(Product.date.desc()).all()

    assert response == [mock_my_model]