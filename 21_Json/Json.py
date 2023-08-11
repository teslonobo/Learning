# Use json module to work with JSON data
import json

# Create a JSON
a =  '{ "name":"John", "age":30, "city":"New York"}'

# Parse a
b = json.loads(a)
print(b["city"])

# Convert Python object into JSON
c = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
d = json.dumps(c)
print(d)
# The result is a JSON string

# Convert Python object containing all the legal data types
e = {
  "name": "John",
  "age": 30,
  "married": False,
  "divorced": True,
  "children": ("Jenny","Jamie"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(e))

# Format the results
f = json.dumps(e, indent=4)
print(f)