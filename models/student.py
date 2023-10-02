from .user import UserModel
from app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class StudentModel(UserModel):
    __tablename__ = 'students'
    #parents is the name of the table
    parent_id = db.Column(db.String(16), db.ForeignKey('parents.id'), nullable=True)
    parent = db.relationship('ParentModel', back_populates='children', primaryjoin='StudentModel.parent_id == ParentModel.id')
    grade = db.Column(db.Integer, nullable=True)

    def __init__(self, id, firstname, lastname, email, date_of_birth, password, parent_id, grade):
        super().__init__(id, firstname, lastname, email, date_of_birth, password)
        self.parent_id = parent_id
        self.grade = grade