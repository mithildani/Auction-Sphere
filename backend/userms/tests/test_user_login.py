from userms.controllers import UserLogin
from userms.tests.mockmodels import request_context, mock_get_sqlalchemy, mock_user_1, mock_login_data_1, \
	mock_login_data_2


def test_user_login_success(
	request_context,
	mock_get_sqlalchemy,
	mock_user_1,
	mock_login_data_1
):
	with request_context(json=mock_login_data_1):
		mock_get_sqlalchemy.filter_by.return_value.first.return_value = mock_user_1

		response = UserLogin().post()

		expected_response = "Logged in successfully"

		assert response["message"] == expected_response


def test_user_login_failure(
	request_context,
	mock_get_sqlalchemy,
	mock_user_1,
	mock_login_data_2
):
	with request_context(json=mock_login_data_2):
		mock_get_sqlalchemy.filter_by.return_value.first.return_value = mock_user_1

		response = UserLogin().post()

		expected_response = "Invalid Password!"

		assert response["message"] == expected_response
