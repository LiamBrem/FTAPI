from app import app
from views import userViews

#register parentStudentViews blueprint
app.register_blueprint(userViews.userBP)

if __name__ == "__main__":
    app.run(debug=True)