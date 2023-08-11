# Create a list
animal_list = ["bird", "cat", "dog"]

# Determine the length of the list
print(len(animal_list))

# Create a list with different data types
main_animal_list = ["bird", 10 , True, "cat", 7, False ,"dog", 4, True]

print(main_animal_list)

# Determine the data type of last list created
print(type(main_animal_list))

# Create a list with the list()constructor
pet_list = list(("bird", "cat", "dog")) # note the double round-brackets
print(pet_list)

# Access a certain item
print(pet_list[0])

# Negative indexing
print(pet_list[-1])

# Range of indexing
print(pet_list[0:2])

# Check if an item is present in list
if "chicken" in pet_list:
  print("Yes, 'chicken' is in the pets list") 
else:
  print("not in that list")