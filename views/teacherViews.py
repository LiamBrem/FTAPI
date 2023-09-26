from flask import Flask, jsonify, request, Blueprint
from models.teacher import TeacherModel  # Import your UserModel from models
from app import db
import random, string

teacherBP = Blueprint("teacherBP", __name__)


@teacherBP.route("/teacher/<string:id>", methods=["GET"])
def get_teacher(id):
    # Assuming you want to retrieve a user with a specific ID
    teacher = TeacherModel.query.get(id)
    if teacher:
        return jsonify(
            {
                "message": "success",
                "user_id": teacher.id,
                "name": teacher.lastname,
                "email": teacher.email,
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


@teacherBP.route("/teacher", methods=["POST"])
def create_teacher():
    data = request.get_json()
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    print("HERE")
    # generate a random 16 character long string of letters and digits
    id = makeID()

    newTeacher = TeacherModel(
        id=id, firstname=firstname, lastname=lastname, email=email
    )

    # Assuming you have a database session called db_session to add and commit the user
    db.session.add(newTeacher)
    db.session.commit()

    print("HERE")

    return (
        jsonify(
            {
                "message": "User Created Successfully",
                "user_id": newTeacher.id,
                "first": newTeacher.firstname,
                "last": newTeacher.lastname,
                "email": newTeacher.email,
            }
        ),
        201,
    )
