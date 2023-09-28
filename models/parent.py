from .user import UserModel
from .student import StudentModel
from app import db

class ParentModel(UserModel):
    __tablename__ = 'parents' 
    children = db.relationship('StudentModel', back_populates='parent', foreign_keys=[StudentModel.parent_id])

    def __init__(self, id, firstname, lastname, email, date_of_birth, password):
        super().__init__(id, firstname, lastname, email, date_of_birth, password)