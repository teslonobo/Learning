# Assign multiple variables
greet = "oh Hello there"
name = "Kyle"
state = 'Florida'
age = 20
#or
greet,name,state,age = "oh Hello there","Kyle","Florida",20
# String variables can be declared with single or double quotes

# Print all of the variables
print(greet, "my name is" , name , "Im", age, "and I live in", state )
# or 
print(f"{greet} my name is {name}, I'm {age} and I live in {state}")

# Assign One Value to multiple variables
a = b = c = "Food"
print(a)
print(b)
print(c)

# Assign varible to Multi-line string
a = """multi line 
string can be done 
with double quotes"""
print(a)
# or
b = '''multi line
string can be done 
with single quotes 
as well'''
print(b) 

#Several Techniques to make Variable names with multiple words easier to read
#camelCase
myVariableName = "Sydney"
#PascalCase
MyVariableName = "Sydney"
#snake_case
my_variable_name = "Sydney"