# School Interface One

## What We're Building
```
Ridgemont High Student Interface 
--------------------------------
Welcome, Lisa. Your access lever is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individul Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit
```

For this challenge we will be building a simple interface for a school that will keep track of student records. There are many ways to create the functionality we are looking for and you should feel free to experiment beyond the scope of this tutorial. We'll be using the menu above as a guide. By the end we'll be able to see a list of students, view individual student data, and create and delete records. We'll also add a simple authentication system. 

#### A Quick Note
This tutorial is pretty comprehensive but it is also meant to challenge you. Some steps are deliberately vague to force you to do your own research and debugging. Don't get discouraged! Help each other out. 

## Our files 

Right now we only have two `ruby` files and a folder for our `csv` files. There is a new file here we may not have seen before called a 'runner' file. For our purposes, the runner file will be the file we 'run' when we want to use our school interface. 

```Ruby 
    #runner.rb
    require_relative 'school'
    school = School.new('Ridgemont High') 

    p school.name
```
Notice the `require_relative` at the top. In order to keep our code organized, we separate our classes and modules into their own files. We can bring code from one file into another file by using `require_relative` followed by a string with the name of the file we want to require. Run `ruby runner.rb` in the command line. You'll get an error because we haven't finished writing our school class yet. Let's do that now. 



## Release 0: Create Classes


```Ruby
# school.rb 

class School 

    def initialize(name, address)
        @name = name
        @address = address
        @students = []
        @staff = []
    end 
end 
```
We'll start by initializing our school with a name and address. Feel free to add other attributes as well. Notice that the school will also be responsible for keeping track of students and staff. Since these will be large collections of objects, we'll use an array to hold them. For now, we'll initialize with empty arrays. Later we'll see how to get our student records loaded right into the class when we start our program. 

#### Students and Staff
Now we can create our student and staff classes. Using the headers in the corresponding CSV files as a guide, we can see what attributes make up a student or staff member and create instance variables accordingly. 


```Ruby 
# student.rb 
class Student 
    def initialize(name, age, password, role, school_id)
        @name = name 
        @age = age         
        @password = password
        @role = role
        @school_id = school_id
    end 
end 
```
```Ruby
#staff.rb
class Staff 
    def initialize(name, age, password, role, staff_id)
        @name = name 
        @age = age         
        @password = password
        @role = role
        @staff_id = staff_id
    end 
end 
```

Uh oh. That's a LOT of repeated code. There's got to be a way to refactor this. Looks like right now students and staff only differ when it comes to how their ids are stored and labeled. As our program develops, we may discover other differences, so it's a good idea to keep these separate classes, but we do want to keep our code as DRY as possible. 

Let's create a `Person` class and move any shared attributes there. Then, set up your `Staff` and` School` classes so that they inherit from `Person`. 

## Release 1: Refactor with .fetch 

The code in our classes is much cleaner now. Let's do one more refactor before we move on. Right now, when we initialize an instance of `Staff` or `Student` we have to pass in five arguments.
```Ruby
Student.new('Diana', 17, 'password', 'Student', 12345)
```
This is ok for now, but as we build out our program we might want to start adding even more attributes. Also, the way our code is now, we need to be careful about the order we pass our args in. If we pass name in last in the example above, then the student_id would get set to `'Diana'`. Not good. 

What would be better is if we could just pass a hash of attributes and have our class work out what goes where. 
```Ruby 
student_info = {name: 'Diana', password: 'password', student_id: 12345, age: 17, role: 'Student'}
Student.new(student_info)
```
This will help us a lot when we start to build out our user interface. Also, notice that order of arguments doesn't matter. All we need to do is set up our class to accept a hash and then pull each value from the hash based on the key. 
```Ruby 
# person.rb 
class Person
    def initialize(args)
        @name = args[:name] 
        @age = args[:age]         
        @password = args[:password]
        @role = args[:role]
    end 
end 
```
This is good, but we may encounter a problem. Try creating a new instance of the `Student` class using a hash, but don't provide a name attribute. What happens? Everything seems to work fine, but if we call `.name` (assuming we've set up the appropriate `attr` methods) we'll see that it is set to `nil`. Sometimes that will be what we want, but this is not one of those times. For our purposes, we want `Ruby` to throw an error when attributes are missing. We can do that by using the  `.fetch` method to grab values from our hash. 
```Ruby 
# person.rb 
class Person
    def initialize(args)
        @name = args.fetch(:name)
        @age = args.fetch(:age)
        @password = args.fetch(:password)
        @role = args.fetch(:role)
    end 
end 
```
Now if we try to create an instance of the `Person` class without providing a name we should get an error telling us exactly which attribute is missing. Refactor the rest of our classes to take a hash and use fetch to retrieve the values. 

#### Move Classes Into Class Folder

Great! One last refactor. Now we have a lot of files hanging around in our root directory. That's not bad, but just for the sake of oranization, let's create a folder just for our classes and move them all in there. Your file structure should look something like this now. 
```
.
├── data                    
│   ├── staff.CSV         
│   └── student.csv                
├── classes                  
│   ├── student.rb         
│   ├── staff.rb         
│   ├── person.rb         
│   └── school.rb 
│               
└── runner.rb 
```

## Release 2: Loading Data
The next thing we need to do is load in our data from the `csv` file using Ruby's `CSV` module. If you haven't done so already, [Read this great article on CSV and Ruby](https://www.sitepoint.com/guide-ruby-csv-library-part/). 
We're going to make a design choice here and say that our `Student` class will be in charge of talking to our student 'database'. To do so, we'll define a [class method](http://www.rubyfleebie.com/2007/04/09/understanding-class-methods-in-ruby). 

Write a method, `all` that returns an array of student objects that represent each row in the `students.csv` file. 

```Ruby
Student.all # => [#<Student:0x00007fe6708cecf0 @name="Lisa", @age="25", @password="xx ", @role="Student", @school_id="13345">, ... ]
```

## Release 3: Loading Staff and Students into School
Again we are making a design decision here that might need to change as we expand functionality. For now, we want each instance of `School` to load in all the `Students` and `Staff` on its own. 

Luckily we did most of the work in the last release. 

```Ruby
# school.rb

def initialize(name, address = nil)
    @name = name 
    @address = address   
    @students = Students.all 
    @staff = Staff.all  
end 
```
That's it! Now we should be able to run our runner file and have a school full of staff and students. This will be the foundation we build the rest of our program around. 

```Ruby 
# runner.rb 
require_relative './classes/school.rb' 

school = School.new('Ridgemont High', '1212 Main st.')

p school.students # => a list of student objects
p school.staff # => a list of staff objects 
```


