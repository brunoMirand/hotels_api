from flask import Flask
from flask_restful import Api
from resources.hotel import Hotels, Hotel


app = Flask(__name__)
app.config.from_object('config')

api = Api(app)

api.add_resource(Hotels, '/hotels/')
api.add_resource(Hotel, '/hotels/<string:hotel_id>')


if __name__ == '__main__':
    app.run()