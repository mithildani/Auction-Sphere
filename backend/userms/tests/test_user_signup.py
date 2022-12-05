from userms.controllers import UserSignup
from userms.tests.mockmodels import request_context, mock_get_sqlalchemy, mock_new_user_1, mock_db


def test_user_signup(
	request_context,
	mock_get_sqlalchemy,
	mock_new_user_1,
	mock_db
):
	with request_context(json=mock_new_user_1):
		mock_get_sqlalchemy \
			.filter_by.return_value \
			.first.return_value = None

		response = UserSignup().post()
		expected_response_msg = "Added successfully"

		assert response["message"] == expected_response_msg
