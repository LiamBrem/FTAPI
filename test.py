import requests
from app import app, db
from models.user import UserModel
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker


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

    parent_data = {
    "firstname": "John",
    "lastname": "Doe",
    "email": "johndoe@example.com",
    "role": "parent",
    "date_of_birth": "2000-01-01", 
    "password": "securepassword",   
    }

    response = requests.post(f'{BASE_URL}/user', json=parent_data)
    if response.status_code == 201:
        print("Parent user created successfully!")
        print(response.json())
    else:
        print("Error creating student user:")
        print(response.status_code)
        print(response.content)



def checkDB():
    app.app_context().push()

    db.create_all()

    engine = create_engine('postgresql://liambrem:pass@localhost:5432/ft')
    Session = sessionmaker(bind=engine)
    session = Session()
    metadata = MetaData()
    metadata.reflect(bind=engine)
    
    tableNames = metadata.tables.keys()

    for table_name in tableNames:
        table = metadata.tables[table_name]
        print(f"Table: {table_name}")
        for column in table.columns:
            print(f"  Column: {column.name} - Type: {column.type}")


checkHttp()




#print all entries from database
#users = UserModel.query.all()
#for user in users:
#    print(user.username)

