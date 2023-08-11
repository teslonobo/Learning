# Python does not have built-in support for Arrays, Lists can be used instead
# To work with arrays in Python you will have to import a library, like NumPy 
# For the sake of these examples we will use lists

# Create a list
hi_end = ["Gucci","Prada","Vendi","Blueburry"]

# Access the elements of an Array
best = hi_end[0]
print(best)

# Modify the value of an Array item
hi_end[0] = "Armani"
best = hi_end[0]
print(best)

# Find the length of an Array
x = len(hi_end)
print(x)

# Looping through Array elements
for z in hi_end:
    print(z)

# Add to an Array
hi_end.append("Gucci")
print(hi_end)

# Remove from an Array
hi_end.pop(3)
print(hi_end)