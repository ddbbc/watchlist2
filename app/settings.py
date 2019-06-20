import sys
import os

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


SQLALCHEMY_DATABASE_URI = prefix + os.path.join(os.path.dirname(__file__), 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'dev'