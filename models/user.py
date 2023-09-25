from app import db 

class UserModel(db.Model):
    id = db.Column(db.String(80), unique=True, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email