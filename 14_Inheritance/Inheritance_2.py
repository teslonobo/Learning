# Create a Parent class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def printname(car):
        print(car.brand, car.model)

c = Car("Toyota", "Corolla")
c.printname()

# Create Child class that inherit Parent class
class Luxury(Car):
    pass
l = Luxury("Cadilac", "Escalade")
l.printname()
# or
class Exotic(Car):
    def __init__(self, brand, model):
        Car.__init__(self, brand, model)

e = Exotic("Ferrari", "Enzo")
e.printname()
# or by using super() function
class Electric(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
x = Electric("Lucid", "Ocean")
x.printname()

# Add a property and method
class Electric(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.modelyear = year
    def selection(car):
        print(f"Great choice in selecting the {car.modelyear} {car.brand} {car.model}")
x = Electric("Lucid", "Ocean", 2023)
x.selection()
# If you add a method in the child class with the same name as a function 
# in the parent class, the inheritance of the parent method will be overridden.