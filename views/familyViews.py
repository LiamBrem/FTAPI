from flask import Flask, jsonify, request, Blueprint

from app import app, mongo

familyBP = Blueprint("familyBP", __name__)

# create a post route that allows the user to link a student and a parent together and then it adds it to a family document in the database
#this should be allowed to have more than 1 parent and 1 student per family
@familyBP.route("/family/create_family", methods=["POST"])
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
@familyBP.route("/family/update_family", methods=["PUT"])
def update_family():
    data = request.get_json()
    student_id = data.get("student_id")
    parent_id = data.get("parent_id")

    collection = mongo.db.families
    

    return jsonify({"message": "Family Updated Successfully"}), 201
