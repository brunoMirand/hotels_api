from database import db


class UserModel(db.Model):
    __tablename__  = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    login = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(40))

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    @classmethod
    def fetch_all(cls):
        users = cls.query.all()
        user = [user.json() for user in users]
        return user

    @classmethod
    def find_user_by_id(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None

    @classmethod
    def find_user_by_login(cls, login):
        user = cls.query.filter_by(login=login).first()
        if user:
            return user
        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'login': self.login
        }
