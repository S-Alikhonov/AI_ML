import re
import uuid
from flask_restful import Resource
from utils.models.tasks import db,Tasks
from flask import request
import json
from datetime import date, datetime
class HomeRoute(Resource):
    def get(self):
        tasks = db.session.query(Tasks).all()
        tasks = [ task.to_json() for task in tasks]
        
        return {'tasks':tasks}
    
    def post(self):
        id = str(uuid.uuid4())
        title = request.form['title']
        description = request.form['description']
        task = Tasks(task_id=id,title=title,description=description)
        
        db.session.add(task)
        db.session.commit()
        
        
        return {'added_task': task.to_json()}
 

class TaskById(Resource):
    def get(self,task_id):
        task = db.session.query(Tasks).filter(Tasks.task_id==task_id).first()
        if task:
            return {'task': task.to_json()}
        else:
            return {'message':'no file exists with such id '},404

    def put(self,task_id):
        task = db.session.query(Tasks).filter(Tasks.task_id==task_id).first()
        if task:
            for key in request.form.keys():
                setattr(task,key,json.loads(request.form[key]))
                setattr(task,'changed_at',datetime.now())
            print(task.completed)
            db.session.commit()
            return {"task edited":task.to_json()}
        
        else:
            return {'message':'no task with such id'},404
        
    def delete(self,task_id):
        task = db.session.query(Tasks).filter(Tasks.task_id==task_id).first()
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'message':'task has been deleted successfully'}
        else:
            return {'message':'no task exists with such id'}