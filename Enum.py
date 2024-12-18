from enum import Enum

"""
An enum (short for "enumeration") in Python is a special data type that allows you to define a set of 
named constants. It provides a way to group related values together under a single type, making your 
code more readable and maintainable. Enums are useful when you have a fixed set of options or categories.
"""

class Status(Enum):
    PENDING = 1
    COMPLETED = 2
    FAILED = 3

def process_order(status: Status):
    if status == Status.PENDING:
        print("Order is being processed...")
    elif status == Status.COMPLETED:
        print("Order is completed!")
    elif status == Status.FAILED:
        print("Order processing failed.")
    else:
        print("Unknown status.")

# Example usage
process_order(Status.PENDING)  # Output: Order is being processed...
# process_order(Status(4))  # Raises ValueError: 4 is not a valid Status


status = Status(2)
print(status)