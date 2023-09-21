from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from views import parentStudentviews

app = Flask(__name__)

app.register_blueprint(parentStudentviews.user_bp)



@app.route("/")
def index():
    return "index"

@app.route("/getUser/<id>", methods=["GET"])
def getUser(id):
    return jsonify({"id": id})


@app.route("/createUser", methods=["POST"])
def createUser():
    data = request.get_json()
    return jsonify(data)    



if __name__ == "__main__":
    app.run(debug=True)