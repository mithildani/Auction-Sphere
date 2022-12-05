from userms.controllers import User
from userms.tests.mockmodels import request_context, mock_get_sqlalchemy, mock_user_1, mock_user_2


def test_get_user_details_0(
    mocker, request_context, 
    mock_get_sqlalchemy,
    mock_user_1,
):

    with request_context():
        request_mock = mocker.patch('userms.request')
        mock_get_sqlalchemy.get.return_value = mock_user_1

        response = User().get(user_id=1)
        expected_response = mock_user_1.to_dict()

        assert response.json == expected_response
