from flask import Flask,render_template,request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import atexit
import json
from jinja2 import Template
from crawler import mycrawler
from inverted import inverted_index
from processor import query_processor


scheduler = BackgroundScheduler()
scheduler.add_job(func=mycrawler, trigger="interval", start_date=datetime(2022,12,12),days=60)
scheduler.start()
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown(wait=False))


file1 = open('data/database.json')
data = json.load(file1)
inverted_index(data)
file2 = open('data/inv_index.json')
index = json.load(file2)

app = Flask(__name__)

@app.route('/',)
def home():
    return render_template('index.html')

@app.route('/search',methods=['POST'])
def get_query():
    query = request.form["query"]
    retrieved = query_processor(data,query,index)
    length = len(retrieved)
    return render_template('result.html',data=data,query=query,retrieved=retrieved,length=length)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=8000)