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
##### Getter Methods
After you've set up the attributes in initialize, run the runner file. It won't work. Read the error. It looks like ruby can't read the our name attribute. But we can see it set right there! 

Turns out instance variables can't be read directly outside of the class. We need to write a method that returns the varaible. Lets do that now. 

```Ruby
    def name
        @name
    end
```
Now we have a method that returns the instance variable.  Now run our runner file and you should see the school's name print to the terminal. 

```Ruby
    p school.name  # => 'Ridgemont High'
```
So now we are calling a method on our school object and that method is what is returning the instance variable that contians the school name. This type of method is so common that it has a name. It is called a 'getter method', becasue it 'gets' the varaible for us. 

##### Setter Methods
Similar to getter methods are setter methods. These methods allow us to update or change instance variables. Setter methods are always named the name of the variable you want to change followed by an equal sign. 

```Ruby 
    def name=(newValue)
        @name = newValue
    end 
```
#### Create the Students and Staff

Now take what you've learned and create a class for students and a class for staff. Think about what attributes each will have. At minimuim include name, and age for both. What would we want to know about staff? What would we need to know about each student? Be sure to include getter and setter methods for each. Require the files in you runner and write code to test that you can create objects and access their instance variables. 

NOTE: You may notice that are code is kind of jumbled. We will be doing some refactoring in our next release. 

