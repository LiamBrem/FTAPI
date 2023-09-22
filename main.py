from app import app, db
from flask_restful import Api

from views import parentStudentViews, teacherViews

app.register_blueprint(parentStudentViews.userBP)


if __name__ == "__main__":
    app.run(debug=True)