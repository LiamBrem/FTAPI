from flask import Flask 
#import pymongo
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/ft"
mongo = PyMongo(app)

