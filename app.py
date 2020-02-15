from flask import Flask
from flask_restful import Api
from app.resources.v1.hotel import Hotels, Hotel
from app.resources.v2.hotel import Hotels as hotels_v2, Hotel as hotel_v2
from app.resources.v2.user import Users, User, Login
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object('config')
jwt = JWTManager(app)
api = Api(app)

# v1 resources
api.add_resource(Hotels, '/v1/hotels/')
api.add_resource(Hotel, '/v1/hotels/<string:hotel_id>')

# v2 resources
api.add_resource(hotels_v2, '/v2/hotels/', endpoint='hotels_v2')
api.add_resource(hotel_v2, '/v2/hotels/<string:hotel_id>', endpoint='hotel_v2')

api.add_resource(Users, '/v2/users/')
api.add_resource(User, '/v2/users/<int:id>', endpoint="user_id")
api.add_resource(Login, '/v2/login/')


@app.before_first_request
def create_database():
    db.create_all()


@app.route('/healthcheck/', methods=['GET'])
def healthcheck():
    return 'OK'


if __name__ == '__main__':
    from database import db
    db.init_app(app)
    app.run(host='0.0.0.0')
