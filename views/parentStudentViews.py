from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api
#import the UserModel from models
from models.user import UserModel
from app import db

userBP = Blueprint("user", __name__)

class User(Resource):
    def get(self, id):
        return {"message": "success"}
    

    def post(self, id,  name, email):
        print("here")
        #get data 
        data = request.get_json()
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")

        new_user = UserModel(id=id, name=name, email=email)


        db.session.add(new_user)
        db.session.commit()

        
        return {"message": "User Created Successfully"}



#initialize the flask restful api using the blueprint
api = Api(userBP)
api.add_resource(User, "/user/<id>/<name>/<email>")
