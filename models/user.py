from app import db 

class UserModel(db.Model):
    id = db.Column(db.String(16), unique=True, primary_key=True)
    firstname = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=True)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, id, firstname, lastname, email, date_of_birth, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.date_of_birth = date_of_birth
        self.password = password