# function - block of reusable code
def add(a, b):
    """Function to add two numbers."""
    c = a + b
    return c 

# lamda function
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Cannot divide by zero"

print("Lambda Calculator:")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    print(f"Addition of {a} + {b}: {add(a, b)}")
    print(f"Subtraction of {a} - {b}: {subtract(a, b)}")
    print(f"Multiplication of {a} * {b}: {multiply(a, b)}")
    print(f"Division of {a} / {b}: {divide(a, b)}")
except ValueError:
    print("Invalid input. Please enter numeric values.") 

# recursive function example
def some_function(n):
    """Recursive function to calculate factorial."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * some_function(n - 1)
n = int(input("Enter a number to calculate its factorial: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {n} is: {some_function(n)}")