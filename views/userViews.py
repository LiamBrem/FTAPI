from flask import Flask, jsonify, request, Blueprint

# import parent, teacher, and student models
from models.user import UserModel
from models.teacher import TeacherModel
from models.student import StudentModel
from models.parent import ParentModel

from app import db, app
import random, string, datetime, jwt

userBP = Blueprint("userBP", __name__)


@userBP.route("/user/<string:id>", methods=["GET"])
def get_user(id):
    # Assuming you want to retrieve a user with a specific ID
    user = UserModel.query.get(id)
    if user:
        return jsonify(
            {
                "message": "success",
                "user_id": user.id,
                "name": user.name,
                "email": user.email,
            }
        )
    else:
        return jsonify({"message": "User not found"}), 404


def makeID():
    # create a 16 character long string of random letters (lowercase & uppercase) and digits
    id = "".join(
        random.choices(
            string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16
        )
    )
    return id


@userBP.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    email = data.get("email")
    role = data.get("role")
    date_of_birth = data.get("date_of_birth")
    password = data.get("password")

    # generate a random 16 character long string of letters and digits
    id = makeID()
    print(id)

    if not id or not firstname or not lastname or not email:
        return jsonify({"message": "Missing required fields"}), 400
    
    print("ROLE:", role)

    if role == "teacher":
        # Teachers require an additional 'subject' parameter
        subject = data.get("subject")

        if not subject:
            return jsonify({"message": "Missing 'subject' field for teacher"}), 400
        newUser = TeacherModel(
            id=id,
            firstname=firstname,
            lastname=lastname,
            email=email,
            date_of_birth=date_of_birth,
            password=password,
            subject=subject,
        )
    elif role == "student":
        # Students require an additional 'grade_level' parameter
        grade = data.get("grade")
        parent_id = data.get("parent_id")

        if not grade:
            return jsonify({"message": "Missing 'grade' field for student"}), 400

        newUser = StudentModel(
            id=id,
            firstname=firstname,
            lastname=lastname,
            email=email,
            date_of_birth=date_of_birth,
            password=password,
            parent_id=parent_id,
            grade=grade,
        )
    elif role == "parent":
        newUser = ParentModel(
            id=id,
            firstname=firstname,
            lastname=lastname,
            email=email,
            date_of_birth=date_of_birth,
            password=password,
        )
    else:
        return jsonify({"message": "Invalid role"}), 400

    # Assuming you have a database session called db_session to add and commit the user
    db.session.add(newUser)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "User Created Successfully",
                "user_id": newUser.id,
                "name": newUser.firstname,
                "email": newUser.email,
            }
        ),
        201,
    )


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

    # check if username and password are correct
    user = UserModel.query.filter_by(username=username).first()
    if user and user.password == password:
        token = generate_token(username)
        return jsonify({"token": token})
    else:
        return jsonify({"message": "Authentication failed"}), 401


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
