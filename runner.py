from classes.school import School 
from classes.student import Student
from classes.person import Person

# school = School('Ridgemont High') 

# print(school.name)

student = Student("name", "age", "role", "password", "school_id")
student.load_students() #need parenthesis to actually call the method
print(student.all_students()) #same here, notice how if you leave out parenthesis you get the method itself, not the method call