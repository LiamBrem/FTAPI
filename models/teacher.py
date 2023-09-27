from app import db
from .user import UserModel

class TeacherModel(UserModel):
    __tablename__ = 'teacher'

    subject = db.Column(db.String(80), nullable=True)

    def __init__(self, id, firstname, lastname, email, date_of_birth, password, subject):
        super().__init__(id, firstname, lastname, email, date_of_birth, password)
        self.subject = subject