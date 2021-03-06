from utils.db import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(255),nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(150),nullable=False,unique=True)
    
    def to_json(self):
        return {
            'id':self.id,
            'first_name':self.first_name,
            'last_name':self.last_name,
            'email':self.email
        }