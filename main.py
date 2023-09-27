from app import app, db
from views import userViews

#register parentStudentViews blueprint
app.register_blueprint(userViews.userBP)
app.register_blueprint(teacherViews.teacherBP)

if __name__ == "__main__":
    app.run(debug=True)