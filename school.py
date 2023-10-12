class School:
    def __init__(self, name) -> None:
        self.name = name
        self.staff = []
        self.students = []

class Person:
    def __init__(self, name, age, role, password) -> None:
        self.name = name
        self.age = age
        self.password = password
        self.role = role

class Student(Person):
    def __init__(self, name, age, role, password, school_id) -> None:
        super().__init__(name, age, role, password)
        self.school_id = school_id

class Staff(Person):
    def __init__(self, name, age, role, password, employee_id) -> None:
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

