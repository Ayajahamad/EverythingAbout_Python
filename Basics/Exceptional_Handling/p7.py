# Custom Exceptions: You can define custom exception classes by inheriting from the built-in Exception class.

class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("This is a custom exception")
except MyCustomError as e:
    print("Custom exception:", e)
