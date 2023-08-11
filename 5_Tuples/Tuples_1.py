# Create a Tuple 
tuple_example = ("apple", "banana", "cherry")
# A tuple is a collection which is ordered and unchangeable and are written with round brackets.
print(tuple_example)

# Determine length of tuple
print(len(tuple_example))

# Create a tuple with one item
my_tuple = ("orange",)
print(type(my_tuple))

# Create a tuple with different data types
my_2nd_tuple = ("xyz", 30, True, 35, "male", "female" )

# Create a tuple with tuple() constructor
my_3rd_tuple = tuple(("apple", "banana", "cherry")) 
print(my_3rd_tuple)

# Access tuple items
print(my_3rd_tuple[2])

# Negative indexing
print(my_3rd_tuple[-1])

# Range of indexes
print(my_3rd_tuple[0:2])

# Check if value is in tuple 
if "apple" in my_3rd_tuple:
  print("Yes, 'apple' is in the fruits tuple") 

# Add to a tuple 
z = list(my_3rd_tuple)
z.append("mango")
my_3rd_tuple = tuple(z)
print(type(my_3rd_tuple))
#tuples can not be changed once created, to do so we convert to a list first, then back to a tuple once list is appended