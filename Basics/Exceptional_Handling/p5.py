# Finally Block: The finally block is always executed, regardless of whether an exception occurs or not. It is used to release external resources or perform cleanup operations.

try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError exception
    print("Division by zero is not allowed")
finally:
    # Cleanup code that always executes
    print("Execution completed")
