# Unpacking a tuple
animals = ("dog", "cat", "mouse")

(big, little, tiny) = animals

print(big)
print(little)
print(tiny)

# Using an Asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# Loop through a tuple
for x in fruits:
  print(x)

# Loop through the index numbers
for i in range(len(fruits)):
  print(fruits[i]) 

# Using a while loop
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1 

# Join two tuples
final_tuple = animals + fruits
print(final_tuple)

# Multiple tuples
my_tuple = fruits * 2
print(my_tuple)