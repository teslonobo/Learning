# Booleans only return True or False

print(15 > 4)
print(20 == 7)
print(14 < 6) 

# Running in an if statement returns True or False
a = 400
b = 20

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

# Evalute Varible/Values
x = "Cheers Mate"
y = 10

print(bool(x))
print(bool(y))

# The following will return False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 