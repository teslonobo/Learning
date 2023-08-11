# Make a copy of a list
fruit_list = ["apple", "banana","cherry","kiwi"]
favorite_list = fruit_list.copy()
print(favorite_list)
# or 
favorite_list = list(fruit_list)
print(favorite_list)

# Join two lists
amount_eatten = [1,4,2,5]
joined_list = fruit_list + amount_eatten
print(joined_list)
# or 
for x in amount_eatten:
  fruit_list.append(x)

print(fruit_list) 
# or 
favorite_list.extend(amount_eatten)
print(favorite_list)