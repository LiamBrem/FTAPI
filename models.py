class User:
    def __init__(self, firstname, lastname, email, password, date_of_birth):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth

class Student(User):
    def __init__(self, firstname, lastname, email, password, date_of_birth, parent_id, grade):
        super().__init__(firstname, lastname, email, password, date_of_birth)
        self.parent_id = parent_id
        self.grade = grade

class Parent(User):
    def __init__(self, firstname, lastname, email, password, date_of_birth):
        super().__init__(firstname, lastname, email, password, date_of_birth) 

class Teacher(User):
    def __init__(self, firstname, lastname, email, password, date_of_birth):
        super().__init__(firstname, lastname, email, password, date_of_birth)