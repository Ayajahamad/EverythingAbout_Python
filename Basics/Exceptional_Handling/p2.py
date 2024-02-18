# Multiple Except Blocks: You can have multiple except blocks to handle different types of exceptions.

try:
    # Code that might raise an exception
    result = int("abc")
    r = 10/0
    print(r)
except ValueError:
    # Handling the ValueError exception
    print("Invalid input for conversion to int")
except ZeroDivisionError:
    # Handling the ZeroDivisionError exception
    print("Division by zero is not allowed")
