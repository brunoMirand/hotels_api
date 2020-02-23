import os.path
from datetime import timedelta


DEBUG = True

BASEDIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

JWT_SECRET_KEY = 'saturday-night-fever'
JWT_ERROR_MESSAGE_KEY = 'message'
JWT_HEADER_TYPE = 'Travolta'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=50)
JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
