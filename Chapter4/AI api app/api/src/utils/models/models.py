from utils.models.db import db 


class UpImage(db.Model):
    __tablename__ = 'input'
    id = db.Column(db.Integer,primary_key=True)
    filename=db.Column(db.Text,nullable=False)
    uploaded=db.Column(db.DateTime,nullable=False,default=db.func.now())
    result = db.relationship('Result',backref='origin')
    

class Result(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    filename=db.Column(db.Text,nullable=False)
    origin_id = db.Column(db.Integer,db.ForeignKey('input.id'),nullable=False)