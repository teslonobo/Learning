# Unpack a collection
animals = ["cat", "dog", "bird"]
a, b, c = animals
print(a)
print(b)
print(c)

# Global Variable use in and out of functions
x = "best"

def sentence_end():
    print("Python is the " + x)
sentence_end()

print("Python is the "+ x)

# Setting Global Variable within function
def this_function():
    global x 
    x = "greatest"
this_function()

print("Python is the " + x)