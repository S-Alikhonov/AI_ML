from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

class Tasks(db.Model):
    task_id = db.Column(db.String(32),primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    description = db.Column(db.String(512),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=db.func.now())
    
    def to_json(self):
        return {
            'task_id':self.task_id,
            'title':self.title,
            'description':self.description,
            'created_at':str(self.created_at)
        }
    