import requests
from app import app, db
from models.user import UserModel

BASE = "http://127.0.0.1:5000/"
app.app_context().push()

db.create_all()

user_data = {
    "id": -1,
    "name": "Liam",
    "email": "email@example.com"
}

response = requests.post(BASE + "user", json=user_data)

# Print the response content and status code for debugging
print(response.json())
print("Response Status Code:", response.status_code)




#print all entries from database
users = UserModel.query.all()
for user in users:
    print(user.username)

