# Create a Class and Object
class my_first_class:
    x = 100
p1 = my_first_class()
print(p1.x) 

# The example above of a class and object is in their simplest form, 
# and are not really useful in real life applications.

# Create a class and use the __init__() function to assign values
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c1 = Car("Toyota","Prius")
print(c1.brand)
print(c1.model)
# The __init__() function is called automatically every time the
# class is being used to create a new object.

# Creat a class and use the __str__() function 
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"{self.brand}({self.model})"

c1 = Car("Toyota","Prius")
print(c1)
# If the __str__() function is not set, 
# the string representation of the object is returned