from .user import UserModel
from app import db

class ParentModel(UserModel):
    __tablename__ = 'parents' 
    def __init__(self, id, username, email, date_of_birth, password):
        super().__init__(id, username, email, date_of_birth, password)