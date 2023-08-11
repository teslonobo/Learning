# Create a function
def test_function():
    print("This is just a test")

# Call the function
test_function()

# Create a function with an argument
def last_name(f_name):
    print(f_name + " Taylor ")

last_name("John")
last_name("Melvin")
last_name("Kyle")

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Create a function with multiple arguments
def name(f_name,l_name):
    print(f_name + " " + l_name)

name("Bud", "Light")
# if you try to call function with 1 argument it will cause an error

# Create a function for an unknown number of arguments
def oldest(*kids):
    print("My oldest kid is " + kids[3])

oldest("Kelly","Jamie","Sam","Jesse")

# Create a function with keyword aruments
def youngest(child_3, child_2, child_1, child_4):
  print("The youngest kid is " + child_3)

youngest(child_1 = "Kelly", child_2 = "Jesse", child_3 = "Jamie", child_4= "Sam") 