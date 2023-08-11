# Create a set 
my_set =  {"apple", "banana", "cherry"}
print(my_set)
# True and 1 are considered the same value in a set

# Duplicates will be ignored
my_set =  {"apple", "banana", "cherry","apple"}
print(my_set)

# Get the length of the set
print(len(my_set))

# Create a set with different datatypes
my_2nd_set = {"abc", 34, True, 40, "male"} 

# Check the type of new set
print(type(my_2nd_set))

# Create a set using set() constructor 
this_set = set(("apple", "banana", "cherry")) 
print(this_set) 

# Access items in set
for x in this_set:
    print(x)

# Check to see if value is in set
print("banana" in this_set)

# Add to a set 
this_set.add("mango")
print(this_set)

# Add from another set or list
tropics = {"pineapple","mango","starfruit"}
tundra = ["ice", "more ice"]
this_set.update(tropics,tundra)
print(this_set)