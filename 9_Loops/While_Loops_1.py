# Create a while loop
i = 2
while i <= 6:
    print(i)
    i += 2

# Create a break statement
i = 2
while i <= 8:
    print(i)
    if i == 4:
        break
    i += 2

# Create a continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Create a else statement
i = 1
while i < 10:
  print(i)
  i += 1
else:
  print("man i is no longer smaller than 10")