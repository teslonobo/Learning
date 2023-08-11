# Create a statement that will generate an exception
try:
    print(x)
except:
    print("Bruv an exception occurred")
# without the try, it will raise an error, because x is not defined

try:
    print(x)
except NameError:
    print("x is not defined")
except:
    print("some other error bruv")

# Create an else statement to execute if there is no errors
try:
    print("Yo")
except:
    print("Bruv it went wrong")
else:
    print("You good bruv")

# Create using a finally block 
try:
    print(x)
except:
    print("something went wrong bruv")
finally:
    print("the try except finished mate")

# Raise an exception
x = -1

if x < 0:
  raise Exception("Sorry, its below zero buddy") 

# Raise a TypeError
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers bruv") 

# Try to open and write to a file 

try:
  f = open("demo.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file") 