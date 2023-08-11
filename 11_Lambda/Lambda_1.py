# Create a lambda function 
x = lambda c : c + 10 
print(x(4))

# Create a lambda function with multiple arguments
y = lambda a, b : a * b
print(y(6,7))

z = lambda d, e, f : d + e + f
print(z(5, 6, 2)) 

# Create a lambda function within a function
def test(n):
    return lambda h : h * n 
double = test(2)
triple = test(3)
print(double(10))
print(triple(10))