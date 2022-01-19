import imp
from flask import Flask
from flask_restful import Api, Resource
from routes.home.route import HomeRoute,ById
from utils.db import db




def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    db.create_all(app=app)

    api.add_resource(HomeRoute, '/')
    api.add_resource(ById,'/<string:id>')
    
    return app