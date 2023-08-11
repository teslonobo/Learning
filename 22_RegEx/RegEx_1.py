# To use regular expressions in Python we have to import module
import re

# Check a string using search
txt = "I said good day"
x = re.search("^I.*day*",txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

# Check a string using findall 
g = re.findall("go", txt)
print(g)

# Return an empty list
f = re.findall("snapple",txt)
print(f)

# Check for the first white-space character 
h = re.search("\s",txt)
print(h)

# Check for each white-space character 
i = re.split("\s",txt)
print(i)

# Using split check for the first white-space
j = re.split("\s",txt,1)
print(j)

# Replace white-space with a number 
k = re.sub("\s", "10",txt)
print(k)

# Print a string passed into the function
txt = "The rain in Spain"
l = re.search(r"\bS\w+",txt)
print(l.string)