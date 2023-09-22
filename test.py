import requests
from app import app, db
from models.user import UserModel

BASE = "http://127.0.0.1:5000/"
app.app_context().push()

db.create_all()

response = requests.post(BASE + "user/1/liam/email")
print(response.json())




#print all entries from database
users = UserModel.query.all()
for user in users:
    print(user.username)

#app.app_context().pop()