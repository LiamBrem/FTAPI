from flask import Flask, jsonify, request, Blueprint

from app import app, mongo
import random, string, datetime, jwt
from models import Student, Teacher, Parent

userBP = Blueprint("userBP", __name__)


@app.route("/user/get_user_id", methods=["GET"])
def get_student_id():
    data = request.get_json()
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    role = data.get("role")

    # select the collection based on the role
    if role == "student":
        collection = mongo.db.students
    elif role == "teacher":
        collection = mongo.db.teachers
    elif role == "parent":
        collection = mongo.db.parents
    else:
        return jsonify({"message": "Invalid role"}), 400

    # Query the MongoDB collection to find the student by first and last name
    user_data = collection.find_one({"firstname": firstname, "lastname": lastname})

    if user_data:
        user_id = str(user_data["_id"])
        return f"The ID of {firstname} {lastname} is {user_id}"
    else:
        return f"No user found with the name {firstname} {lastname}"


@userBP.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    email = data.get("email")
    date_of_birth = data.get("date_of_birth")
    password = data.get("password")

    role = data.get("role")

    if not firstname or not lastname or not email:
        return jsonify({"message": "Missing required fields"}), 400

    print("ROLE:", role)

    if role == "teacher":
        # create new teacher
        collection = mongo.db.teachers
        new_user = Teacher(firstname, lastname, email, password, date_of_birth)
    elif role == "student":
        # create student
        collection = mongo.db.students
        new_user = Student(
            firstname,
            lastname,
            email,
            password,
            date_of_birth,
            data.get("parent_id"),
            data.get("grade"),
        )
    elif role == "parent":
        collection = mongo.db.parents
        new_user = Parent(firstname, lastname, email, password, date_of_birth)
    else:
        return jsonify({"message": "Invalid role"}), 400

    result = collection.insert_one(new_user.__dict__)
    return jsonify({"message": f"{role} Created Successfully"}), 201


# Token generation function
def generate_token(username):
    payload = {
        "sub": username,
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(minutes=30),  # Token expiration time
    }
    token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")
    return token


# make a login functoin that uses a token-based authentication system
@userBP.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")


# Protected route
# API Endpoints: In a RESTful API, the /protected route might represent a specific API endpoint
# that provides access to a resource. For instance, it could be used to retrieve a list of user-specific items,
# create new items, update existing ones, or perform other CRUD (Create, Read, Update, Delete) operations.
### IN this program, this can be used to access the user's information
@userBP.route("/protected", methods=["GET"])
def protected_resource():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token is missing"}), 401

    try:
        payload = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        return jsonify({"message": "Welcome, {}".format(payload["sub"])})
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401
