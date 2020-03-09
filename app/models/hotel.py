from database import db


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
