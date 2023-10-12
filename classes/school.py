from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.staff = Staff.load_staff()
        self.students = Student.load_students()