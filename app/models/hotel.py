from database import db
from connection import ConnectionDatabase


class HotelModel(db.Model):
    __tablename__ = 'hotels'

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    stars = db.Column(db.Float(precision=1))
    daily_rate = db.Column(db.Float(precision=2))
    city = db.Column(db.String(40))

    def __init__(self, hotel_id, name, stars, daily_rate, city):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.daily_rate = daily_rate
        self.city = city

    @classmethod
    def fetch_all(cls):
        hotels = cls.query.all()
        hotel = [hotel.json() for hotel in hotels]
        return hotel

    @classmethod
    def find_hotel_by_id(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first()
        if hotel:
            return hotel
        return None

    @classmethod
    def find_hotel(cls, params_url, params):
        database = cls.connection_database()

        city_parameter = ''
        if params_url.city:
            city_parameter = 'city = ? AND '

        query = 'SELECT * FROM hotels \
                        WHERE {} \
                            (stars >= ? AND stars <= ?) \
                                LIMIT ? OFFSET ?'.format(city_parameter)
        database.execute(query, params)
        hotels = cls.format_result_in_json(database.fetchall())

        return hotels

    @classmethod
    def format_result_in_json(cls, hotels):
        list_hotels = []
        for hotel in hotels:
            list_hotels.append({
                'hotel_id': hotel[1],
                'name': hotel[2],
                'start': hotel[3],
                'dailu_rate': hotel[4],
                'city': hotel[5],
            })

        return list_hotels

    @classmethod
    def connection_database(cls):
        return ConnectionDatabase().connection_database()

    def save_hotel(self):
        db.session.add(self)
        db.session.commit()

    def update_hotel(self, name, stars, daily_rate, city):
        self.name = name
        self.stars = stars
        self.daily_rate = daily_rate
        self.city = city

    def delete_hotel(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'hotel_id': self.hotel_id,
            'name': self.name,
            'stars': self.stars,
            'daily_rate': self.daily_rate,
            'city': self.city
        }
