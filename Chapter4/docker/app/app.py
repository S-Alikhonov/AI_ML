from flask import Flask
import flask_restful
from utils.db import db
from flask_restful import Api
from routes.route import AllRecords

def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLACHEMY_TRACK_MODIFICATION'] = True
    db.init_app(app) #intilize the database
    db.create_all(app=app) # creates all tables 
    
    api.add_resource(AllRecords,'/')
    return app

if __name__ == '__main__':
    appl = create_app()
    appl.run('0.0.0.0')