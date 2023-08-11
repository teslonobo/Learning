# Create a variable that belongs to the local scope of a function
def try_it():
  x = 40000
  print(x)
try_it() 

# Function inside a function
def test_1():
  x = 30
  def test_inner():
    print(x)
  test_inner()
test_1()

# Create a variable that belongs to the global scope
x = 20
def test_2():
  print(x)
test_2()
print(x)

# Same named variables that belong to global and local scope 
x = 420
def test_3():
  x = 710
  print(x)
test_3()
print(x)
# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables, one available in 
# the global scope (outside the function) and one available in the local scope (inside the function)

# Create a global scope with in a function
def test_4():
  global x
  x = 666
  print(x)
test_4()
print(x)

# Change a global scope from within a function
x = 200
print(x)
def test_5():
  global x 
  x = 250
  print(x)
test_5()
print(x)
