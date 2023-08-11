# Return an Iterator from a Iterable 
pets = ("cat","dog","goldfish","bird")
my_it = iter(pets)

print(next(my_it))
print(next(my_it))
print(next(my_it))
# Lists, tuples, dictionaries, and sets are all 
# iterable objects even strings.

# Looping through an Iterator
for x in pets:
    print(x)
# The for loop actually creates an iterator object 
# and executes the next() method for each loop

# Create an Iterator
class My_Numbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

my_class = My_Numbers()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Create an Iterator with a StopIteration
class My_Numbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 4:
       x = self.a
       self.a += 1
       return x
    else:
      raise StopIteration

my_class = My_Numbers()
my_iter = iter(my_class)

for x in my_iter:
  print(x)