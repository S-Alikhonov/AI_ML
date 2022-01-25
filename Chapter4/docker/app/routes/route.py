from flask_restful import Resource
from utils.models import User
from utils.db import db
from flask import request

class AllRecords(Resource):
    def get(self):
        users = db.session.query(User).all()
        users = [user.to_json() for user in users]
        return {'users':users}
    
    def post(self):
        user = User()
        for key in request.form.keys():
            setattr(user,key,request.form[key])
            
        db.session.add(user)
        db.session.commit()
        return {'user':user.to_json()}
            
        