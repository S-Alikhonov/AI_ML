import os 

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATION = False
SQLALCHEMY_DATABASE_URI = os.environ('DATABASE_URL','sqlite://')