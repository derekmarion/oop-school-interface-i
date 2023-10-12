from Person import Person
class Staff(Person):
    def __init__(self, name, age, role, password, employee_id) -> None:
        super().__init__(name, age, role, password)
        self.employee_id = employee_id