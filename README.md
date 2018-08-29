# School Interface One

## Overview

For this challenge we will be building a simple interface for a school that will keep track of student and staff records. 

##Our files 

Right now we only have two files. We will have many more by the time we are done. For now, we just have a file to hold our school class and a new file we may not have seen before called a 'runner' file. For our purposes the runner file will be the file we 'run' when we want to use our school interface. 

```Ruby 
    #runner.rb
    require_relative 'school'

    school = School.new('Ridgemont High') 

    p school.name
```
Notice the 'require_relative' at the top. In order to keep our code organized, we seperate our classes and modules into their own files. We can bring code from one file into another file by using require_relative followed by a string with the name of the file we want to require. Run `ruby runner.rb` in the command line to run the file. You'll get an error because we havn't finished writing our school class yet. Let's do that now. 

#### Create the School Class

Write the code that will create a new school object.
Think about what attributes a school should have. What should the school object know? For now, make sure your school object at least has a name, location, and a way to store students and staff. What data structure might be helpful here? 

```Ruby
    class School
        def initialize(name, location)
           @name = name
           @location = location 
           @staff = # what data structure goes here?
           @students = # same
        end 
    end 
```
##### Getter Methods
After you've set up the attributes in initialize, run the runner file. We will get a brand new error! Progress. Ruby can see that we have a school object, but it doesn't seem to know how to access the name attribute.  

Turns out instance variables can't be read directly outside of the class. We need to write a method that returns the varaible. Lets do that now. 

```Ruby
    def name
        @name
    end
```
This type of method is so common that it has a name. It is called a 'getter method', becasue it 'gets' the varaible for us. It often has the same name as the variable it is returning. Now run the runner file and you should see the school's name print to the terminal. 

```Ruby
    p school.name  # => 'Ridgemont High'
```
To recap, we are calling a method on our school object and that method is what is returning the instance variable that contians the school name. 

##### Setter Methods
Similar to getter methods are setter methods. These methods allow us to update or change instance variables. Setter methods are always named the name of the variable you want to change followed by an equal sign. 

```Ruby 
    def name=(new_value)
        @name = new_value
    end 
```

In your runner, try to change the name of the school and print the result. 

```Ruby 
    school = School.new('Ridgemont High') 

    p school.name

    school.name = 'Starbucks International College Prep High School of Science and Technology Sponsored by Old Spice' 

    p school.name
```

##### Add Getter and Setter for location
Not all variables will require getters and setters. Some might need one or the other, some might not need any at all. We will want to access the school location for our program and it is concevalbe that the school might move to a new building so lets add a getter and setter for location to our School class. 
```Ruby
    def locatoin
        # your code here
    end 

    def locatoin=(new_locatoin)
        # your code here
    end
```
#### Create the Student and Staff Classes

Now take what you've learned and create a class for students and a class for staff. Think about what attributes each will have. At minimuim include name, and age for both. What would we want to know about staff? What would we need to know about each student? Be sure to include getter and setter methods for each. Require the files in you runner and write code to test that you can create objects and access their instance variables. 

NOTE: You may notice that are code is kind of jumbled. We will be doing some refactoring in our next release. 

