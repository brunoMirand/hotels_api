from flask_restful import Resource
from app.models.user import UserModel
from app.resources.request_parser import RequestParser
from flask_jwt_extended import create_access_token
from werkzeug.security import safe_str_cmp


class Users(Resource):
    def get(self):
        users = UserModel.fetch_all()
        return users, 200

    def post(self):
        body = RequestParser().get_body_users_args()
        user = UserModel.find_user_by_login(body['login'])
        if user:
            return {'message': 'User %s already exists' % body['login']}, 422
        new_user = UserModel(**body)
        try:
            new_user.save_user()
        except:
            return {'message': 'cannot save user, internal server error'}, 500
        return new_user.json(), 201


class User(Resource):
    def get(self, id):
        user = UserModel.find_user_by_id(id)
        if user:
            return user.json(), 200
        return {'message': 'user not found'}, 404


class Login(Resource):
    def post(self):
        body = RequestParser().get_body_users_args()
        user = UserModel.find_user_by_login(body['login'])
        if user and safe_str_cmp(user.password, body['password']):
            token = create_access_token(identity=user.id)
            return {'access token': token}, 200
        return {'message': 'The username or password is incorrect'}, 401
