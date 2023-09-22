from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from views import parentStudentViews, teacherViews


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://liambrem:pass@localhost:5432/ft"
db = SQLAlchemy(app)

api = Api(app)

app.register_blueprint(parentStudentViews.userBP)


if __name__ == "__main__":
    app.run(debug=True)