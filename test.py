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

    response = requests.post(f'{BASE_URL}/user', json=teacher_data)
    if response.status_code == 201:
        print("Stuedent user created successfully!")
        print(response.json())
    else:
        print("Error creating student user:")
        print(response.status_code)
        print(response.content)

def checkGetUser():
    app.app_context().push()
    student_data = {
        "firstname": "John",
        "lastname": "Doe",
    }

    response = requests.get(f'{BASE_URL}/user/get_student_id', json=student_data)
    print(response.content)




#checkHttp()
checkGetUser()  


