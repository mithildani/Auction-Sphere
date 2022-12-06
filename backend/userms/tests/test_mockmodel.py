from userms.models import Users
from userms.tests.mockmodels import mock_my_model, mock_get_sqlalchemy


def test_sqlalchemy_query_property_get_mock(
        mock_my_model,
        mock_get_sqlalchemy,
):
    mock_get_sqlalchemy.all.return_value = [mock_my_model]
    response = Users.query.all()

    assert response == [mock_my_model]
