# Generic Except Block: You can also use a generic except block to catch any exception that is not handled by preceding except blocks.

try:
    # Code that might raise an exception
    result = int("abc")
except ValueError:
    # Handling the ValueError exception
    print("Invalid input for conversion to int")
except:
    # Handling any other exception
    print("An error occurred")
