# Change a Value within a list
fruit_list = ["apple", "banana", "cherry"]
fruit_list[1] = "mango"
print(fruit_list)

# Change a range of values within a list
fruit_list[1:3] = ["peach", "watermelon"]
print(fruit_list)

# Insert a new value to a list
fruit_list.insert(2, "grapes")
print(fruit_list)

# Add new value to end of the list
fruit_list.append("kiwi")
print(fruit_list)

# Append two lists together
pest_list = ["ants","mosquitos"]
fruit_list.extend(pest_list)
print(fruit_list)

# Remove a specificed value
fruit_list.remove("kiwi")
print(fruit_list)

# Remove a specified index, if not specified will remove last on list
fruit_list.pop(1)
print(fruit_list)
# or
del fruit_list[4]
print(fruit_list)
# or to delete the whole list add no brackets 

# Clear a list
pest_list.clear()
print(pest_list)