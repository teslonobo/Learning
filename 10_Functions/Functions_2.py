# Create a function for an unkown number of keyword arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Kyle", lname = "Taylor") 

# Create a function using default parameter value
def location(country = "Cuba"):
  print("I am located in " + country)

location("Finland")
location("England")
location()
location("Canda")

# Pass a list as an argument
def fav_fruits(food):
  for x in food:
    print(x)

fruits = ["kiwi", "strawberry", "pineapple", "banana"]

fav_fruits(fruits)

# Return Values 
def some_maths(x):
  return 5 * x
print(some_maths(5))
print(some_maths(10))
print(some_maths(20))

# Create an empty function
def test():
  pass
# Trick function defintions cant be left empty to avoid error we use pass

# Create a recursive function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)