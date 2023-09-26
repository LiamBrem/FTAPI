from flask import Flask, jsonify, request, Blueprint
from models.user import UserModel  # Import your UserModel from models
from app import db
import random, string

userBP = Blueprint('userBP', __name__)


@userBP.route('/user/<string:id>', methods=['GET'])
def get_user(id):
    # Assuming you want to retrieve a user with a specific ID
    user = UserModel.query.get(id)
    if user:
        return jsonify({"message": "success", "user_id": user.id, "name": user.username, "email": user.email})
    else:
        return jsonify({"message": "User not found"}), 404
    

def makeID():
    # create a 16 character long string of random letters (lowercase & uppercase) and digits
    id = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))
    return id


@userBP.route('/user/<username>/<email>', methods=['POST'])
def create_user(username, email):
    print(username,email)

    # generate a random 16 character long string of letters and digits
    id = makeID()
    print(id)

    if not id or not username or not email:
        return jsonify({"message": "Missing required fields"}), 400

    newUser = UserModel(id=id, username=username, email=email)

    # Assuming you have a database session called db_session to add and commit the user
    db.session.add(newUser)
    db.session.commit()

    print("HERE")

    return jsonify({"message": "User Created Successfully", "user_id": newUser.id, "name": newUser.username, "email": newUser.email}), 201

