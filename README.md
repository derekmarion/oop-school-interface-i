# School Interface One

## What We're Building
```
Ridgemont High Student Interface 
--------------------------------
Welcome, Richard. Your access level is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit
```

For this challenge we will be building a simple interface for a school that will keep track of student records. There are many ways to create the functionality we are looking for and you should feel free to experiment beyond the scope of this tutorial. We'll be using the menu above as a guide. By the end we'll be able to see a list of students, view an individual student's data, and create and delete records. We'll also add a simple authentication system. 

#### A Quick Note
This tutorial is pretty comprehensive but it is also meant to challenge you. Some steps are deliberately vague to force you to do your own research and debugging. Don't get discouraged! Help each other out. 

## Our files 

Right now we only have two Python files and a `data` folder for our CSV files. There is a new file here we may not have seen before called a **runner** file. For our purposes, the runner file will be the file we 'run' when we want to use our school interface. 

```Python 
#runner.py
from school import School  

school = School('Ridgemont High') 

print(school.name)
```
Notice the import statement at the top. In order to keep our code organized, we separate our classes and modules into their own files. We can bring code from one file into another file by using `from <file_name> import <class_name>`. Run `python runner.py` in the command line. You'll get an error because we haven't finished writing our school class yet. Let's do that now. 


## Release 0: Create Classes

```Python
# school.py
class School:
    def __init__(self, name):
        self.name = name
        self.staff = []
        self.students = []
```
We'll start by initializing our school with a name. Feel free to add other attributes as well. Notice that the school will also be responsible for keeping track of students and staff. Since these will be large collections of objects, we'll use a list to hold them. For now, we'll initialize with empty lists. Later, we'll see how to get our student records loaded right into the class when we start our program. 

#### Students and Staff
Now we can create our student and staff classes. Using the headers in the corresponding CSV files as a guide, we can see what attributes make up a student or staff member and create instance variables accordingly. 


```Python 
# student.py
class Student:
    def __init__(self, name, age, role, school_id, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role
        self.school_id = school_id
```
```python
#staff.py
class Staff:
    def __init__(self, name, age, role, employee_id, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role
        self.employee_id = employee_id
```

Uh oh. That's a LOT of repeated code. There's got to be a way to refactor this. Looks like right now students and staff only differ when it comes to how their ids are stored and labeled. As our program develops, we may discover other differences, so it's a good idea to keep these separate classes, but we do want to keep our code as DRY as possible. 

Let's create a `Person` class and move any shared attributes there. Then, set up your `Staff` and` School` classes so that they inherit from `Person`. [Read about how inheritance works here.](https://www.python-course.eu/python3_inheritance.php) We'll cover it in more detail tomorrow.


## Release 1: Refactor with dict and **kwargs

The code in our classes is much cleaner now. Let's do one more refactor before we move on. Right now, when we initialize an instance of `Staff` or `Student` we have to pass in five arguments.

```Python
Student('Diana', 17, 'password', 'Student', 12345) # Arguments input in the correct order
```
This is ok for now, but as we build out our program we might want to start adding even more attributes. Also, the way our code is now, we need to be careful about the order we pass our args in. If we pass name in last in the example above, then the school_id would get set to `'Diana'`. Not good. 

```Python
Student(17, 'password', 'Student', 12345, 'Diana') # Arguments input in the incorrect order
```

What would be better is if we could just pass a dictionary of attributes and have our class work out what goes where. Turns out Python has a built in way for us to do just that. 

```python 
student_info = {'name' : 'Diana', 'password' : 'password', 'school_' : 12345, 'age' : 17, 'role' : 'Student'}
Student(**student_info)
```

This will help us a lot when we start to build out our user interface. Also, notice that order of arguments doesn't matter. 

#### How it works 
When we prepend the `**` to an argument it acts sort of like a spread operator in Javascript. Python functions can take arguments as values (these are called `args`),but they can also take them as keyword values (called `kwargs`). The `**` unpacks the dictionary and passes each key value pair in as a kwarg. 

```Python
# args the way we have been using them. The position of the argument determines what variable the value gets assigned to. 
Student('Diana', 17, 'password', 'Student', 12345)

# using keyword arguments lets us not have to worry about order. 
Student(school_id=12345, age=17, password='password', role='Student',  name='Diana')

```

The keyword argument example above is essentially what happens when we pass a dictionary to our School object. 

```Python 
student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
Student(**student_info)

# the ** before student_info turns this: 
    # {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# Into this:
    #  name='Diana', password='password', school_id=12345, age=17, role='Student'

```
#### Move Classes Into Class Folder

Great! One last refactor. Now we have a lot of files hanging around in our root directory. That's not bad, but just for the sake of organization, let's create a folder just for our classes and move them all in there. Your file structure should look something like this now. This may change the way you need to import some files. Read up on how python handles [importing code from other files](https://www.blog.pythonlibrary.org/2016/03/01/python-101-all-about-imports/) to help you solve any issues that might come up. 
```
.
├── data                    
│   ├── staff.csv         
│   └── student.csv                
├── classes                  
│   ├── student.py         
│   ├── staff.py         
│   ├── person.py         
│   └── school.py 
│               
└── runner.py 
```

## Release 2: Loading Data
The next thing we need to do is load in our data from the `CSV` file using Python's `CSV` module. If you haven't done so already, [Read over the Python CSV docs](https://docs.python.org/3/library/csv.html). 
We're going to make a design choice here and say that our `Student` class will be in charge of talking to our student 'database'. To do so, we'll define a [class method](https://realpython.com/instance-class-and-static-methods-demystified/#static-methods). 

Write a method, `all_students()` that returns an array of student objects that represent each row in the `students.csv` file. 

```Python
Student.all_students() # => [<__main__.Student object at 0x10c4fa908>, <__main__.Student object at 0x10c4faa58>, <__main__.Student object at 0x10c4faba8>, <__main__.Student object at 0x10c4facf8>, <__main__.Student object at 0x10c4fae48>, <__main__.Student object at 0x10c4faf98>]
```
#### Hint 
You'll need to import `os.path` and use `os.path.abspath` as well as `os.path.join` to read from the `csv` file. 

```Python
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/students.csv")
    
with open(path) as csvfile:

```

## Release 3: Loading Staff and Students into School
Again we are making a design decision here that might need to change as we expand functionality. For now, we want each instance of `School` to load in all the `Students` and `Staff` on its own. 

Luckily, we did most of the work in the last release. 

```Python
# school.py

def __init__(self, name):
    self.name = name   
    self.students = Students.all_students() 
    self.staff = Staff.all_staff()
```
That's it! As long as we remembered to import our staff and student classes, we'll be all set. Now we should be able to run our runner file and have a school full of staff and students. This will be the foundation we build the rest of our program around. 

```Python 
# runner.py 
from classes.school import School 

school = School('Ridgemont High') 

print(school.staff) 

print(school.students)
```


