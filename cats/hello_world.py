from flask import Flask
from pymongo import MongoClient
import random

client = MongoClient('mongodb', 27017)
db = client.data
collection = db.zips
app = Flask(__name__)

@app.route('/')
def hello_world():
    zip = get_random_zip()
    #print zip['city']
    return zip['city']

def get_random_zip():
    count = collection.count()
    return collection.find()[random.randrange(count)]  

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
