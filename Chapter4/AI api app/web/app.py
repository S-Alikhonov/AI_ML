from importlib.metadata import files
from unittest import result
from flask import Flask,render_template,request,redirect,url_for,flash
import os
from os.path import dirname,realpath,join
from werkzeug.utils import secure_filename
import json
from json import loads
import requests
from models.db import db
from models.model import UpImage
import uuid
# url = 'http://172.19.0.2:8000/'
url = 'http://localhost:8000/'

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1111@localhost/images'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'
db.init_app(app)
db.create_all(app=app)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER  = join(dirname(realpath(__file__)), 'static/uploads/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

   
@app.route('/',methods=['POST','GET'])
def file():
    if request.method=="POST":
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
        if file and allowed_file(file.filename):
            filename = f'{uuid.uuid4()}.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
            image = UpImage(filename=f'{UPLOAD_FOLDER}{filename}')
            db.session.add(image)
            db.session.commit()
            
            data = requests.post(f'{url}',data={'image_id':image.id})
            jsn= loads(data.content)
            number = jsn['number']
            mask = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five',
                    '6':'six','7':'seven','8':'eight','9':'nine'}
            numbers = [mask[i] for i in number]
            image = jsn['image']
            results = jsn['results']
            return render_template('result.html',number=number,numbers=numbers,image=filename,results=results,iter=len(results))
        
    return render_template('file.html',page_title='File upload')




if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
    app.run(debug=True,host='0.0.0.0')