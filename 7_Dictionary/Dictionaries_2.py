# Add to a dictionary
car = {
"brand": "Tesla",
"model": "Model 3",
"year": 2022
}
x = car.keys()
print(x) # Before the change
car["color"] = "white"
print(x) # After the change 

# Get Values
y = car.values()
print(y)

# Get Items
z = car.items()
print(z)

# Check if key exists
if "model" in car:
  print("Yes, 'model' is one of the keys in the dictionary") 

# Change Value
car["year"] = 2023
print(car["year"])

# Update dictionary
car.update({"year": 2021})
print(car["year"]) 

# Remove items from a dictionary
car.pop("model")
print(car)
# or 
del car["year"]

# Empty a dictionary 
car.clear()
print(car)
