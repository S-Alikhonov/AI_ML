from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config.from_object('api.config.Config')
db = SQLAlchemy(app)

class Striver(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    email = db.Column(db.String(155),unique=True,nullable=False)
    name = db.Column(db.String(155),unique=False,nullable=True)
    
    

class Striver_api(Resource):
    
    def get(self):
        args_parser = reqparse.RequestParser()
        args_parser.add_argument('email',type=str)
        args = args_parser.parse_args()
        email = args['email']
        try:
            user = db.session.query(Striver).filter_by(email=email).first()
            return {"name":user.name,"email":user.email}
        except:
            return {"email":"couldn't find record with given email"}
    
    def post(self):
        args_parser = reqparse.RequestParser()
        args_parser.add_argument('email',type=str)
        args_parser.add_argument('name',type=str)
        
        args = args_parser.parse_args()
        email = args['email']
        name = args['name']
        try:
            db.session.add(Striver(name=name,email=email))
            db.session.commit()
            return {"email":email, 'name':name}
        except:
            return {"message":"couldn't insert record into database with given data"}
api.add_resource(Striver_api,'/')