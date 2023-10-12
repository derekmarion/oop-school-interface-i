from Person import Person
class Student(Person):
    def __init__(self, name, age, role, password, school_id) -> None:
        super().__init__(name, age, role, password)
        self.school_id = school_id