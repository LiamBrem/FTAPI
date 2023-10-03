import requests
from app import app

BASE_URL = "http://127.0.0.1:5000"


def checkHttp():
    app.app_context().push()
    student_data = {
    "firstname": "Liam",
    "lastname": "Brem",
    "email": "johndoe@example.com",
    "role": "student",
    "date_of_birth": "2000-01-01", 
    "password": "securepassword",
    "parent_id": "1234567890123456",
    "grade": "11",    
    }

    teacher_data = {
    "firstname": "John",
    "lastname": "Doe",
    "email": "johndoe@example.com",
    "role": "teacher",
    "date_of_birth": "2000-01-01", 
    "password": "securepassword",   
    }

    response = requests.get(f'{BASE_URL}/user', json=teacher_data)
    if response.status_code == 201:
        print("Stuedent user created successfully!")
        print(response.json())
    else:
        print("Error creating student user:")
        print(response.status_code)
        print(response.content)

def checkMakeFam():
    app.app_context().push()
    data = {
        "family_id": "651c5d6390e91140d159b1c8",
        "user_id": "651b06db9517256db536f5f2",
        "role": "student",
    }

    response = requests.put(f'{BASE_URL}/family/update_family', json=data)
    print(response.content)




checkMakeFam()

