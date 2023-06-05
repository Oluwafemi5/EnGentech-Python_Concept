def add(x, y):

    result = x + y

    return f"The addition of {x} and {y} = {result}"

def subtract(x, y):

    result = x - y

    return f"The subtraction of {x} and {y} = {result}"

def divide(x, y):

    if y == 0:

        return "Error: Cannot divide by zero"

    result = x / y

    return f"The division of {x} and {y} = {result}"

def multiply(x, y):

    result = x * y

    return f"The multiplication of {x} and {y} = {result}"

def mod(x, y):

    if y == 0:

        return "Error: Cannot calculate remainder with zero"

    result = x % y

    return f"The remainder of {x} divided by {y} = {result}"

print(add(5, 2))

print(multiply(4, 3))

print(divide(6,2))

print(subtract(5,12))

print(mod(17,2))
