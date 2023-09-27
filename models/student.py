from .user import UserModel
from app import db
#import mappend_column
from sqlalchemy.orm import mapped_column

class StudentModel(UserModel):
    __tablename__ = 'students'
    #parents is the name of the table
    parent_id = mapped_column(db.ForeignKey('parents.id')) 
    parent = db.relationship('ParentModel', back_populates='children')
    grade = db.Column(db.Integer, nullable=True)

    def __init__(self, id, firstname, lastname, email, date_of_birth, password, parent_id, grade):
        super().__init__(id, firstname, lastname, email, date_of_birth, password)
        self.parent_id = parent_id
        self.grade = grade