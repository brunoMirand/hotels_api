from flask_restful import Resource
from app.models.hotel import HotelModel
from app.resources.request_parser import RequestParser


hotels = [
    {
        'hotel_id': 'alpha',
        'name': 'Alpha Hotel',
        'stars': 5,
        'daily_rate': 500,
        'city': 'Sao Paulo'
    },
    {
        'hotel_id': 'beta',
        'name': 'Beta Hotel',
        'stars': 4.8,
        'daily_rate': 480,
        'city': 'Sao Paulo'
    },
    {
        'hotel_id': 'gamma',
        'name': 'Gamma Hotel',
        'stars': 4.7,
        'daily_rate': 470.30,
        'city': 'Sao Paulo'
    },
]

class Hotels(Resource):
    def get(self):
        return {'Hoteis': hotels}


class Hotel(Resource):
    def find_hotel_by_id(self, hotel_id):
        for hotel in hotels:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def mount_body(self, hotel_id, body):
        built_body = {
            'hotel_id': hotel_id,
            'name': body['name'],
            'stars': body['stars'],
            'daily_rate': body['daily_rate'],
            'city': body['city']
        }
        return built_body

    def get(self, hotel_id):
        hotel = self.find_hotel_by_id(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found'}, 404

    def post(self, hotel_id):
        if self.find_hotel_by_id(hotel_id):
            return {'message': 'Hotel id %s already exists.' % hotel_id}, 400

        body = RequestParser().get_body_args()
        # new_hotel = self.mount_body(hotel_id, body)
        new_hotel = HotelModel(hotel_id, **body).json()

        hotels.append(new_hotel)
        return new_hotel, 201

    def put(self, hotel_id):
        body = RequestParser().get_body_args()
        # new_hotel = self.mount_body(hotel_id, body)
        new_hotel = HotelModel(hotel_id, **body).json()

        hotel = self.find_hotel_by_id(hotel_id)
        if hotel:
            hotel.update(new_hotel)
            return new_hotel, 200

        hotels.append(new_hotel)
        return hotel, 201

    def delete(self, hotel_id):
        global hotels
        hotels = [ hotel for hotel in hotels if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted'}, 200
