from flask import Flask, jsonify, request, Blueprint

from app import app, mongo
from bson import ObjectId

familyBP = Blueprint("familyBP", __name__)

@familyBP.route("/family/get_family_id", methods=["GET"])
def get_family_id():
    data = request.get_json()
    student_id = data.get("student_id")
    parent_id = data.get("parent_id")

    collection = mongo.db.families

    # query the database for the family with the student and parent
    family_data = collection.find_one({"students": student_id, "parents": parent_id})

    if family_data:
        family_id = str(family_data["_id"])
        return f"The ID of the family with student {student_id} and parent {parent_id} is {family_id}"
    else:
        return f"No family found with student {student_id} and parent {parent_id}"


@familyBP.route("/family/create_family", methods=["POST"])
def create_family():
    data = request.get_json()
    student_id = data.get("student_id")
    parent_id = data.get("parent_id")

    # Check if both student_id and parent_id are provided
    if not student_id or not parent_id:
        return jsonify({"message": "Both student_id and parent_id are required"}), 400

    collection = mongo.db.families

    # Check if the family already exists with the given student_id and parent_id - this may need to be changed if students have more than one family
    existing_family = collection.find_one({"students": student_id, "parents": parent_id})
    if existing_family:
        return jsonify({"message": "Family with this student and parent already exists"}), 400

    
    # Create a new family document with the provided student and parent
    new_family = {
        "students": [student_id],
        "parents": [parent_id]
    }

    result = collection.insert_one(new_family)
    return jsonify({"message": "Family Created Successfully"}), 201

# now make a route that adds a student to an existing family
@familyBP.route("/family/update_family", methods=["PUT"])
def update_family():

    data = request.get_json()
    user_id = data.get("user_id")
    role = data.get("role")
    family_id = ObjectId(data.get("family_id"))

    family = mongo.db.families.find_one({"_id": family_id})

    if not family:
        return jsonify({"message": "Family not found"}), 400

    collection = mongo.db.families

    # make this depending on the role
    if role == "student":
        # add the student to the family
        collection.update_one({"_id": family_id}, {"$addToSet": {"students": user_id}})
    elif role == "parent":
        # add the parent to the family
        collection.update_one({"_id": family_id}, {"$addToSet": {"parents": user_id}})
    else:
        return jsonify({"message": "Invalid role"}), 400
    

    return jsonify({"message": "Family Updated Successfully"}), 201
