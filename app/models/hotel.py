class HotelModel:
    def __init__(self, hotel_id, name, stars, daily_rate, city):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.daily_rate = daily_rate
        self.city = city

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'stars': self.stars,
            'daily_rate': self.daily_rate,
            'city': self.city
        }
