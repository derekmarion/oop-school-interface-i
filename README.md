# School Interface One

## Overview

For this challenge we will be building a simple interface for a school to keep track of students and staff. 

##Our files 
Right now we only have two files. We will have many more by the time we are done. For now, we just have a file to hold our school class and a new file we may not have seen before called a 'runner' file. For our purposes the runner file will be the file we 'run' when we want to user our school interface. 

```Ruby 
    require_relative 'school'

    school = School.new('Ridgemont High') 

    p school.name
```
Notice the 'require_relative' at the top. In order to keep our code organized, we seperate our classes and modules into their own files. We can bring code from one file into another file by using require_relative. This way we can just run `ruby runner.rb` in the command line if we want to print out the schools name. 


#### Create the School Class

Write the code that will create a new school object.
Think about what attributes a school should have. What should the school object know? For now, make sure your school object at least has a name, locations, and a way to store students and staff. What data structure might be helpful for storing students? 

```Ruby
    class School
        def initialize(name)
           @name = name
           @staff = # what data structure goes here?
           @students = # same
        end 
    end 
```
After you've set up the attributes in initialize, run the runner file. It won't work. Read the error. It looks like ruby can't read the our name attribute. But we can see it set right there! 

Turns out instance variables can't be read directly outside of the class. We need to write a method that returns the varaible. Lets do that now. 

```Ruby
    def name
        @name
    end
```
#### Create the Students

Your students will be stored in the school database.  (Don't worry about creating a database - just have a way for the school to store the student's records).

Can you think of anything they might inherit from the school, or is inheritance not needed here? These design decisions are up to you.

#### Create the Staff

There are multiple types of staff, and you're free to create your own.

A few obvious examples are principal, teachers, teaching assistants, receptionists, and janitors.  What attributes and methods might they all share?  What will be different for each?

### Release 1 : Build Authentication System

Now imagine you're delivering this software and it's going to run as a Ruby file in Terminal.

You're going to create a single administrator who can add staff (teachers, janitors, etc) and students, and only this administrator is allowed to create these objects in the system.

You also want to allow the created staff and students to login and access their grades. Remember, a student shouldn't be able to access information about other students or teachers.

An example of how this interface might look (this is just an idea - you are welcome to implement this feature however you think is best):

```text
$ ruby school.rb
> Welcome to Bayside High
> -------------------------------
> Please enter your username:
> richard_belding
> Please enter your password:
> ********
> -------------------------------
> Welcome, richard_belding.  Your access level is: PRINCIPAL
> -------------------------------
> What would you like to do?
> Options:
> - list_students
> - view_grades <student_id>
> - add_grade <student_id>
> - remove_grade <student_id> <grade_id>
```


## Optimize Your Learning

As you are coding, ask yourself...

 * How will I use this class?
 * How will this class interact with the other classes?
 * Does this attribute need to be private or public?
 * Are my methods and variables well named?
 * Am I using the best object type for my variables?