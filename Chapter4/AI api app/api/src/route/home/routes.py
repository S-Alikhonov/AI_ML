from flask_restful import Resource
from flask import request
from route.home.logic import runer
from time import sleep
from utils.models.models import UpImage,Result
from utils.models.db import db
# from logic import runer


class GetFile(Resource):
    def post(self):
        
        res = request.form['image_id']
        image = db.session.query(UpImage).filter(UpImage.id==res).first()
        if image:
            print(image.filename,flush=True)
            number,files = runer(image.filename,'/Users/saidalikhonalikhonov/Desktop/docker_composed/api/src/route/home/model.pth')
            for file in files:
                result = Result(filename=file,origin_id=res)
                db.session.add(result)
            db.session.commit()
                
            return {'number':number,'image':res,'results':files}
        else:
            return {'number':'no image'}
