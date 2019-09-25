# services/users/project/api/users.py

from flask import Blueprint
from flask_restful import Resource, Api

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

# the route handler
class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'dong!'
    }

api.add_resource(UsersPing, '/users/ding')
