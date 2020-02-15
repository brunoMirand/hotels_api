import os.path


DEBUG = True

BASEDIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

JWT_SECRET_KEY = 'super-flash'
