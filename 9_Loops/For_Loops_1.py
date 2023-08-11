# Create a for loop
animals = ["cat","dog","bear","snake"]
for x in animals:
    print(x)

# Create a for loop for a string
for x in "lizard":
    print(x)

# Create a break statement
cars = ["lexus","toyota","nissan","ford","chevy"]
for x in cars:
    print(x)
    if x == "toyota":
        break

# Create a break statement before print
cars = ["lexus","toyota","nissan","ford","chevy"]
for x in cars:
    if x == "toyota":
        break
    print(x)

# Create a continue statement
games = ["gta", "horizon", "halo","2k"]
for x in games:
  if x == "horizon": # wont print horizon
    continue
  print(x)

# Create a range() function
for x in range(11):
    print(x)

# Create a range() function with a start parameter
for x in range(6,11):
    print(x)

# Create a range() function while incrementing the sequence
for x in range(0,11,2):
    print(x)

# Create a else for loop 
for x in range(5):
  print(x)
else:
  print("Finished!") 
# The else block will NOT be executed if the loop is stopped by a break statement

# Create a empty for loop
for x in [0, 1, 2]:
  pass
# Trick for loops cant be empty 