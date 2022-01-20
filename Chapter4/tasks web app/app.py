
from flask import Flask,render_template,request
import json
import requests
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    data = requests.get('http://localhost:8000')
    tasks = json.loads(data.content)
    return render_template('home.html',tasks=tasks['tasks'])

if __name__ == '__main__':
    app.run(debug=True)