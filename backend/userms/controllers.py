from flask import request, jsonify
from flask_restful import Resource

from userms.main.database import db
from userms.models import Users as user_model


class User(Resource):
	def get(self, user_id):
		return jsonify(user_model.query.get(user_id).to_dict())


class UserSignup(Resource):
	def post(self):
		first_name = request.get_json()['firstName']
		last_name = request.get_json()['lastName']

		email = request.get_json()['email']
		contact_number = request.get_json()['contact']

		password = request.get_json()['password']

		new_user_details = {
			"first_name": first_name,
			"last_name": last_name,
			"email": email,
			"contact_number": contact_number,
			"password": password
		}

		response = {}

		email_exists = user_model.query.filter_by(email=email).first() is not None
		contact_number_exists = user_model.query.filter_by(contact_number=contact_number).first() is not None

		if email_exists:
			response["message"] = "An account with this contact already exists"

			return response

		if contact_number_exists:
			response["message"] = "An account with this contact already exists"

			return response

		new_user = user_model(**new_user_details)

		db.session.add(new_user)
		db.session.commit()

		response["message"] = "Added successfully"

		return response


class UserLogin(Resource):
	def post(self):
		email = request.get_json()['email']
		password = request.get_json()['password']

		user = user_model.query.filter_by(email=email).first()

		response = {}

		if user is None:
			response["message"] = "Please create an account!"
		elif user.password != password:
			response["message"] = "Invalid Password!"
		else:
			response["user_id"] = user.id
			response["message"] = "Logged in successfully"

		return response
