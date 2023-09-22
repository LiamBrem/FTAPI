from flask import Blueprint, jsonify, request
from flask_restful import Resource, Api

userBP = Blueprint("user", __name__)
    

listOfStudents = {
    "1": {"name": "Liam", "email": "email:"},
    "2": {"name": "Daws", "email": "email:"},
    "3": {"name": "Brem", "email": "email:"}
}

class User(Resource):
    def get(self, id):
        return listOfStudents[id]
    

    def post(self, name, age):
        new_user = User(name=name, age=age)
        return {"data": "Posted"}



#initialize the flask restful api using the blueprint
api = Api(userBP)
api.add_resource(User, "/user/<id>")
