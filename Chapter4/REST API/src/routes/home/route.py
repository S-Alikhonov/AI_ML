from flask_restful import Resource
from flask import request

class HomeRoute(Resource):
    def get(self):
        return {'message':request.method}

    def post(self):
        data = request.form['text']
        print(data)
        return {'message': request.method}

