from app import app
from views import userViews, familyViews

#register parentStudentViews blueprint
app.register_blueprint(userViews.userBP)
app.register_blueprint(familyViews.familyBP)

if __name__ == "__main__":
    app.run(debug=True)