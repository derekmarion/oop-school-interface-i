from classes.person import Person #notice you have to specify the top level package/folder here, it's not implicit that the modules are in the same package when import to a module in another folder
import csv

class Student(Person):
    def __init__(self, name, age, role, password, school_id) -> None:
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def load_students(cls):
        cls.students = [] #Notice this is a class variable, not an instance variable, so it will be available to all student instances, not declared above init because we don't necessarily want to initalize it when we creat a new student, only when loading all students
        with open("data/students.csv", mode="r") as csv_file:  #filepath is relative to where the method is called
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                new_student = Student(name=row['name'], age=row['age'], role=row['role'], password=row['password'], school_id=row['school_id'])
                cls.students.append(new_student)
        return cls.students

    @classmethod
    def all_students(cls):
        return cls.students