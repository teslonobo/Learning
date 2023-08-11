# Concatentation of strings
a = "Good"
b = "Day"
c = a + b
print(c)

# Add a space between them 
c = a + " " + b
print(c)

# This will cause an error because you can not concatenate an integer and string
age = 22
txt = "My name is John and I am only " + age
print(txt)
# comment out line 12-14

# Insert integer into a string by format method
age = 22
txt = "My name is John and I am only {}"
print(txt.format(age))

# Format takes unlimited number of arguments
quantity = 6
itemno = 5367
price = 9.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
