import requests
from app import app, db
from models.user import UserModel

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker


def checkHttp():
    BASE = "http://127.0.0.1:5000/"
    app.app_context().push()

    db.create_all()

    user_data = {
        "name": "Dawson",
        "email": "email.com"
    }

    response = requests.post(BASE + "user", json=user_data)

    # Print the response content and status code for debugging
    print(response.json())
    print("Response Status Code:", response.status_code)


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
users = UserModel.query.all()
for user in users:
    print(user.username)

