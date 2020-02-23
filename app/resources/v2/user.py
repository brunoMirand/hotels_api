from flask_restful import Resource
from app.models.user import UserModel
from app.resources.request_parser import RequestParser
from flask_jwt_extended import (
    create_access_token, get_raw_jwt,
    jwt_required, create_refresh_token,
    jwt_refresh_token_required, get_jwt_identity
)
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST


class Users(Resource):
    @jwt_required
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
    @jwt_required
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
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            token = {
                'access token': access_token,
                'refresh_token': refresh_token
            }
            return token, 200
        return {'message': 'the username or password is incorrect'}, 401


class Logout(Resource):
    @jwt_required
    def post(self):
        token_id = get_raw_jwt()['jti']
        BLACKLIST.add(token_id)
        return {'message': 'successfully logged out'}, 200


class RefreshToken(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        token = {
            'access_token': create_access_token(identity=current_user)
        }
        return token, 200
