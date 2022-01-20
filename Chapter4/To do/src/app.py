
from urllib import request
from flask import Flask,render_template
from flask_restful import Api
from utils.models.tasks import db
from route.home.routes import HomeRoute,TaskById
import json


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCEHMY_TRACK_MODIFICATION'] = True
    db.init_app(app)
    db.create_all(app=app)
    
    api.add_resource(HomeRoute,'/')
    api.add_resource(TaskById,'/<string:task_id>')
    
    
    return app
