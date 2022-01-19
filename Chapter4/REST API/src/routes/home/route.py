import imp
from unittest import result
from flask_restful import Resource
from flask import request
import uuid
from utils.model import User
from utils.db import db

database = []
class HomeRoute(Resource):
    def get(self):
        users = db.session.query(User).all()
        users = [user.to_json() for user in users]
        return {'users':users}

    def post(self):
        id = str(uuid.uuid4())
        name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        user = User(id=id,first_name=name,last_name=last_name,email=email)
        db.session.add(user)
        db.session.commit()
        return {'user':user.to_json()}

def findById(id):
    result = None
    for data in database:
        if id == data['id']:
            result = data
    return result



class ById(Resource):
    def get(self,id):
        user= db.session.query(User).filter(User.id==id).first()
        if user:
            return {'user':user.to_json()}
        else :
            return {'message':'not found'},404
    
    def put(self,id):
        user = db.session.query(User).filter(User.id==id).first()
        if user:
            for key in request.form.keys():
                setattr(user,key,request.form[key])
            db.session.commit()
            return {'user':user.to_json()}
        else:
            return {'user':'there is no user with current id'},404
    
    def delete(self,id):
        user = db.session.query(User).filter(User.id==id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message':'user deleted successfully'}
        else:
            return {'user':'there is no user with current id'},404