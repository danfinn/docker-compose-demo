from flask import Flask
from pymongo import MongoClient
client = MongoClient('mongodb', 27017)
db = client.data
collection = db.zips
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

def get_random_zip()
    zip = collection.aggregate( { $sample: { size: 1 } } )

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
