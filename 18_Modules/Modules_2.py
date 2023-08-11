# Use Module and create an alias
import Modules_1 as mx

mx.greeting("Kyle")

# Access dictionary
a = mx.person1["age"]
print(a)

# Import only the dictionary
from Modules_1 import person1
print(person1["age"])