# Remove a item in a set 
my_set =  {"apple", "banana", "cherry","apple"}
my_set.remove("banana")
print(my_set)
# or 
my_set.discard("cherry")
print(my_set)

# Clear a set
my_set.clear()
print(my_set)

# Delete set completely
my_set = {"apple", "banana", "cherry"}
del my_set
print(my_set)
# This will raise an error because there is no set 
# Comment out line 15

# Loop through a set 
for x in my_set:
  print(x) 

# Join two sets 
set_1 = {"cats","dogs","birds"}
set_2 = {1,2,3}
set_3 = set_1.union(set_2)
print(set_3)
# or 
set_1.update(set_2)
print(set_1)

# Keep only whats present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z) 

# Keep all but what is present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z) 