from flask import Flask, jsonify, request, Blueprint
from models.user import UserModel  # Import your UserModel from models
from app import db
userBP = Blueprint('userBP', __name__)


@userBP.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    # Assuming you want to retrieve a user with a specific ID
    user = UserModel.query.get(id)
    if user:
        return jsonify({"message": "success", "user_id": user.id, "name": user.name, "email": user.email})
    else:
        return jsonify({"message": "User not found"}), 404


@userBP.route('/user', methods=['POST'])
def create_user():
    print('HERE')
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid input data"}), 400

    id = data.get("id")
    username = data.get("name")
    email = data.get("email")

    if not id or not username or not email:
        return jsonify({"message": "Missing required fields"}), 400

    newUser = UserModel(id=id, username=username, email=email)

    # Assuming you have a database session called db_session to add and commit the user
    db.session.add(newUser)
    db.session.commit()

    return jsonify({"message": "User Created Successfully", "user_id": newUser.id, "name": newUser.username, "email": newUser.email}), 201

