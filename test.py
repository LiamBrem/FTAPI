import requests
from app import app


def checkHttp():
    app.app_context().push()
    BASE_URL = "http://127.0.0.1:5000"
    student_data = {
    "firstname": "John",
    "lastname": "Doe",
    "email": "johndoe@example.com",
    "role": "student",
    "date_of_birth": "2000-01-01", 
    "password": "securepassword",
    "parent_id": "1234567890123456",
    "grade": "10",    
    }

    teacher_data = {
    "firstname": "John",
    "lastname": "Doe",
    "email": "johndoe@example.com",
    "role": "teacher",
    "date_of_birth": "2000-01-01", 
    "password": "securepassword",   
    }

    response = requests.post(f'{BASE_URL}/user', json=teacher_data)
    if response.status_code == 201:
        print("Teacher user created successfully!")
        print(response.json())
    else:
        print("Error creating student user:")
        print(response.status_code)
        print(response.content)




checkHttp()


