from flask_restful import Resource
from flask import request
from logic import runer



class GetFile(Resource):
    def post(self):
        
        res = request.form['file']
        print(res,flush=True)
        runer(res,'model.pth')
        return {'filename':res}
    
