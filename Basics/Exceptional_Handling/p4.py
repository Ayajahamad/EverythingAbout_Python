# Else Block: The else block is executed if no exception occurs in the try block.
try:
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Handling the ZeroDivisionError exception
    print("Division by zero is not allowed")
else:
    # Executed if no exception occurs
    print("Result:", result)
