from flask import Flask, jsonify, request, Blueprint

from app import app, mongo
import random, string, datetime, jwt
from models import Student, Teacher, Parent

userBP = Blueprint("userBP", __name__)


@app.route('/get_student_id', methods=['GET'])
def get_student_id():
    data = request.get_json()
    firstname = data.get("firstname")
    lastname = data.get("lastname")

    collection = mongo.db.students

    # Query the MongoDB collection to find the student by first and last name
    student_data = collection.find_one({'firstname': firstname, 'lastname': lastname})

    if student_data:
        student_id = str(student_data['_id'])
        return f"The ID of {firstname} {lastname} is {student_id}"
    else:
        return f"No student found with the name {firstname} {lastname}"

# create a post route that allows the user to link a student and a parent together and then it adds it to a family document in the database
#this should be allowed to have more than 1 parent and 1 student per family
@userBP.route("/user/family", methods=["POST"])
def create_family():
    data = request.get_json()
    student_id = data.get("student_id")
    parent_id = data.get("parent_id")

    collection = mongo.db.families
    result = collection.insert_one({
        "student_id": student_id,
        "parent_id": parent_id
    })

    return jsonify({"message": "Family Created Successfully"}), 201

# now make a route that adds a student to an existing family
@userBP.route("/user/family/<string:id>", methods=["PUT"])
def update_family(id):
    data = request.get_json()
    student_id = data.get("student_id")
    parent_id = data.get("parent_id")

    collection = mongo.db.families
    result = collection.update_one({
        "_id": id
    }, {
        "$set": {
            "student_id": student_id,
            "parent_id": parent_id
        }
    })

    return jsonify({"message": "Family Updated Successfully"}), 201




@userBP.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    email = data.get("email")
    role = data.get("role")
    date_of_birth = data.get("date_of_birth")
    password = data.get("password")

    if not firstname or not lastname or not email:
        return jsonify({"message": "Missing required fields"}), 400
    
    print("ROLE:", role)

    if role == "teacher":
        # create new teacher
        collection = mongo.db.teachers
        result = collection.insert_one({
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "date_of_birth": date_of_birth,
            "password": password,
        })

        return jsonify({"message": "Teacher Created Successfully"}), 201
        

    elif role == "student":
        # create student
        collection = mongo.db.students
        result = collection.insert_one({
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "date_of_birth": date_of_birth,
            "password": password,
            "parent_id": data.get("parent_id"),
            "grade": data.get("grade")    
        })

        return jsonify({"message": "Student Created Successfully"}), 201

        
    elif role == "parent":
        #create parent
        pass
    else:
        return jsonify({"message": "Invalid role"}), 400
    
    return jsonify({"message": "User Created Successfully"}), 201




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
