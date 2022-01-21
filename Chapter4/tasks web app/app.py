
from pydoc import describe
from flask import Flask,render_template,request,redirect,url_for
import json
import requests
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    data = requests.get('http://localhost:8000')
    tasks = json.loads(data.content)['tasks']
    return render_template('home.html',tasks=tasks,page_title='tasks app')

@app.route('/create',methods=['POST','GET'])
def create():
    if request.method=='POST':
        title = request.form['title']
        description = request.form['description']
        task = {
            'title':title,
            'description':description
        }
        url = 'http://localhost:8000/'
        requests.post(url,data=task)
        return redirect(url_for('index'))
    else:
        return render_template('create.html',page_title='task creation page')
@app.route('/search',methods=['POST','GET'])
def search():
    
    return render_template('search.html',page_title='task searching page')

@app.route('/task/<string:id>',methods=['POST','GET'])
def task(id):
    url = 'http://localhost:8000'
    task = requests.get(f'{url}/{id}')
    task = json.loads(task.content)['task']
    
    return render_template('task.html',task=task)

@app.route('/task/<string:id>/delete',methods=['POST','GET'])
def delete(id):
    url = 'http://localhost:8000'
    requests.delete(f'{url}/{id}')
    return redirect(url_for('index'))

@app.route('/task/<string:id>/update',methods=['GET','POST'])
def update(id):
    # getting task from api
    url = 'http://localhost:8000'
    task = requests.get(f'{url}/{id}')
    task = json.loads(task.content)['task']
    if request.method == 'GET':
        return render_template('update.html',task=task)
    #when user submits
    else:
        title = request.form['title']
        description = request.form['description']
        task = {
            'title':title,
            'description':description
        }
        url = 'http://localhost:8000/'
        requests.put(f'{url}/{id}',data=task)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)