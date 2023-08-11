# Create an object method 
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def selection(self):
        print("You have seleted the " + self.brand + " " + self.model)

c1 = Car("Toyota","Prius")
c1.selection()
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:
class Car:
    def __init__(check, brand, model):
        check.brand = brand
        check.model = model
    def selection(selected):
        print("You have seleted the " + selected.brand + " " + selected.model)

c1 = Car("Toyota","Prius")
c1.selection()

# Modify an object property
c1.model = "Corolla"
c1.selection()

# Delete object property 
del c1.model

# Delete Object 
del c1

# Create an empty class
class Car:
    pass
# Trick you cant create an empty class but you can use pass to not cause an error