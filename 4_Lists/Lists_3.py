# Loop through a list
fruit_list = ["apple", "banana", "cherry"]
for x in fruit_list:
  print(x) 

# Loop through the index number 
for i in range(len(fruit_list)):
  print(fruit_list[i])

# Using a While Loop
i = 0
while i < len(fruit_list):
  print(fruit_list[i])
  i = i + 1

# Loop using List comprehension
[print(x) for x in fruit_list] 

#Syntax for list comprehension
#newlist = [expression for item in iterable if condition == True]
#Condition is like a filter that only accepts the items that valuate to True.
#Iterable can be any iterable object, like a list, tuple, set etc.
#Expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list.

# Sort a list alphanumerically
fruit_list.sort()
print(fruit_list)

# Sort Descending
fruit_list.sort(reverse=True)
print(fruit_list)

# Perform a case-insentive sort
fruit_list.sort(key = str.lower)
print(fruit_list)

# Reverse the order of the list
fruit_list.reverse()
print(fruit_list)