from flask_restful import Api

from users.controllers import User, UserSignup, UserLogin

api = Api(catch_all_404s=True, prefix='/users/api')

api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserSignup, '/signup')
api.add_resource(UserLogin, '/login')
