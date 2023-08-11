# Use a Polymorph on different objects
a = "Check me out" #string
b = ("cars","boats","motorcycle") #tuple
c = ["bikes","scooters","skates"] #list
d = {
    "Brand": "Honda",
    "Model": "Civic",
    "Year": 2022
} #dictionary

print(len(a)) #returns number of characters
print(len(b)) #returns number of items in tuple
print(len(c)) #returns number of items in list
print(len(d)) #returns number of key/value pairs in dictionary

# Use Polymorhism in Classes
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
class Car(Vehicle):
    def move(self):
        print("Drive!!!")
class Boat(Vehicle):
    def move(self):
        print("Sail!!!")
class Plane(Vehicle):
    def move(self):
        print("Fly!!!")

c1 = Car("Honda","Civic",2022)
b1 = Boat("Ibiza","Touring",2021)
p1 = Plane("Boeing","747",2020)

for x in (c1,b1,p1):
    print(x.brand)
    x.move()

