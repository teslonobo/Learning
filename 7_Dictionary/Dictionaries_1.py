# Create a dictionary
my_dict = {
  "brand": "Tesla",
  "model": "Model 3",
  "year": 2022
}
print(my_dict)

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(my_dict["brand"])

# Find the length of dictionary
print(len(my_dict))

# Create a dictionary with different datatypes
this_dict =	{
  "brand": "Toyota",
  "electric": False,
  "year": 2022,
  "colors": ["red", "white", "blue"]
} 
# Print datatype of dictionary
print(type(this_dict))

# Create a dictionary using the dict() constructor
second_dict = dict(name = "John", age = 30, country = "USA")
print(second_dict)

# Access items in a dictionary
x = second_dict["name"]
# or
y = second_dict.get("country")

# Get keys
z = second_dict.keys()