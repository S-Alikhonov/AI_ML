from importlib.metadata import files
from flask import Flask,render_template,request,redirect,url_for,flash
import os
from os.path import dirname,realpath,join
from werkzeug.utils import secure_filename
import json
import requests
url = 'http://172.19.0.2:8000/'
app=Flask(__name__)

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
            filename = 'images.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            rescontent = {'file':f'{UPLOAD_FOLDER}{filename}'}
            requests.post(f'{url}',data=rescontent)
        
    return render_template('file.html',page_title='File upload')




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')