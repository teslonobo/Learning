# Parent class is the class being inherited from, 
# also called base class.
# Child class is the class that inherits from another class, 
# also called derived class.

# Create a Parent class 
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

a = Person("Sammy", "Fisher")
a.printname()

# Create a Child class
class Teacher(Person):
    pass
# Use the pass keyword when you do not want to add 
# any other properties or methods to the class.

# Use the Child class to create an object
b = Teacher("Doctor","Willis")
b.printname()

# Create a Child Class with the __init__() function
class Student(Person):
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.lastname, self.firstname)
# The child's __init__() function overrides 
# the inheritance of the parent's __init__() function.
s = Student("Sam", "King")
s.printname()