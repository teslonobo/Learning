# Loop through a dictionary
car = {
"brand": "Tesla",
"model": "Model 3",
"year": 2022
}

for x in car:
    print(x)
    # or 
    print(car[x])

# Return values 
for x in car.values():
    print(x)

# Return keys
for x in car.keys():
    print(x)

# Loop through both keys and values
for x, y in car.items():
  print(x, y) 

# Make a copy of dictionary
my_dict = car.copy()
print(my_dict)
# or 
my_dict = dict(car)
print(my_dict)

# Create a Nested dictionary
my_family = {
  "child_1" : {
    "name" : "Sam",
    "year" : 2004
  },
  "child_2" : {
    "name" : "Melvin",
    "year" : 2007
  },
  "child_3" : {
    "name" : "Junior",
    "year" : 2011
  }
} 
# or 
child_1 = {
  "name" : "Sam",
  "year" : 2004
}
child_2 = {
  "name" : "Junior",
  "year" : 2007
}
child_3 = {
  "name" : "Melvin",
  "year" : 2011
}

my_family = {
  "child_1" : child_1,
  "child_2" : child_2,
  "child_3" : child_3
} 

# Access items in Nested dictionaries
print(my_family["child_3"]["name"])