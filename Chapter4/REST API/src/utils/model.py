from email.policy import default
from utils.db import db
import uuid

class User(db.Model):
    id = db.Column(db.String(32),primary_key=True,default=str(uuid.uuid4()))
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(20),nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    
    def to_json(self):
        return {
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'email':self.email,
            'created_at':str(self.created_at)
        }