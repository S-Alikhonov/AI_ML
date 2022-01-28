from flask import Flask
from flask_restful import Api
from route.home.routes import GetFile
import json



def create_app():
    app = Flask(__name__)
    api = Api(app)
 

    
    api.add_resource(GetFile,'/')
    
    
    return app

if __name__ == "__main__":
    appl = create_app()
    appl.run(host='0.0.0.0',port=8000)