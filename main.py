from app import app, db
from views import parentStudentViews, teacherViews

#register parentStudentViews blueprint
app.register_blueprint(parentStudentViews.userBP)

if __name__ == "__main__":
    app.run(debug=True)