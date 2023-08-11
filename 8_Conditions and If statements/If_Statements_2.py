# Create if statement with and keyword
a = 20
b = 800
c = 44
if a < b and c > a: print("Both conditions are True")

# Create if statement with or keyword
if a < b or c < a: print("At least one of the conditions is True")

# Create if statement with not keyword
if not a > b: print("A is NOT greater than B")

# Create a Nested if statement
if c > 10: 
    print("Above 10")
    if c > 20: 
        print("and also above 20!")
    else:
        print("but not above 20")

# Create an empty if statement
if b > a:
    pass
# Trick: if statements cant be empty but if you do for some reason use it put a pass statement
