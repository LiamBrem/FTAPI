from app import app, db
from views import parentStudentViews, teacherViews

#register parentStudentViews blueprint
app.register_blueprint(parentStudentViews.userBP)
app.register_blueprint(teacherViews.teacherBP)

if __name__ == "__main__":
    app.run(debug=True)