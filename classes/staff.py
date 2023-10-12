from classes.person import Person #notice again how the filepath is relative to where the method is called, which is why you need to specify the folder
import csv

class Staff(Person):
    def __init__(self, name, age, role, password, employee_id) -> None:
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    @classmethod
    def load_staff(cls):
        cls.staff = [] #Notice this is a class variable, not an instance variable, so it will be available to all student instances, not declared above init because we don't necessarily want to initalize it when we creat a new student, only when loading all students
        with open("data/staff.csv", mode="r") as csv_file:  #filepath is relative to where the method is called
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                new_staff = Staff(name=row['name'], age=row['age'], role=row['role'], password=row['password'], employee_id=row['employee_id'])
                cls.staff.append(new_staff)
        return cls.staff
                
    @classmethod
    def all_staff(cls):
        return cls.staff