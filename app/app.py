from flask import Flask, render_template
from pymongo import MongoClient
import random
import redis

client = MongoClient('mongodb', 27017)
db = client.data
collection = db.zips
app = Flask(__name__)

r = redis.Redis(host='redis')
r.set('counter','0')

@app.route('/')
def hello_world():
    increment_redis()
    hits = get_redis()
    zip = get_random_zip()
    return render_template('index.html', title='Home', zip=zip, hits=hits)

@app.route('/counter')
def counter():
    return get_redis()

def get_random_zip():
    count = collection.count()
    return collection.find()[random.randrange(count)]  

def increment_redis():
    r.incr('counter',1)
    return

def get_redis():
    value=r.get('counter').decode('utf-8')
    return value

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
