
from flask import Flask
from flask_restful import Api
from route.home.routes import GetFile
import json
from utils.models.db import db



def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1111@localhost/images'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = 'secret string'
    
    api.add_resource(GetFile,'/')
    db.init_app(app)
    db.create_all(app=app)
    
    return app

if __name__ == "__main__":
    appl = create_app()
    appl.run(debug=True,host='0.0.0.0',port=8000)