"""
Decorators in Python are a powerful and flexible tool that allow you to modify or enhance the 
behavior of functions or methods. They are often used to add functionality to existing code in a 
clean and reusable way.
"""
"""
Functions as First-Class Objects: In Python, functions are first-class objects. This means that 
functions can be passed as arguments to other functions, returned as values from other functions, 
and assigned to variables. Decorators leverage this feature.
"""
"""
Define the Outer Function (Decorator): This function will accept the function to be decorated as an argument.
Define the Inner Function (Wrapper): The inner function will call the original function and can add 
    behavior before or after the call.
Return the Inner Function: The outer function returns the inner function, which now wraps the original 
    function.
"""

# Simple Decorator function.
def dec_fun(func):
    def wrapper():
        print("Before Adding Extra functionality..!")
        func()
        print("After Adding Extra functionality..!")
    return wrapper

@dec_fun
def add_func():
    print("--Here added some Fubctionality--")
# add_func()

# Decorator function with Arguments.
    # If you need your decorator to accept arguments, you'll need an additional level of nesting.
def dec_func_with_arg(num):
    def outer_wrapper(func):
        def wrapper(*args,kwargs):
            print("Before..!")
            for _ in range(num):
                func(*args)
            print("After..!")
            # return result
        return wrapper
    return outer_wrapper

@dec_func_with_arg(3)
def say_hello(name):
    print(f"Hello {name}")
# say_hello("Alice")

# Define the Decorator with Arguments
def verbose_logger(verbosity=1):
    def decorator(func):
        def wrapper(*args, kwargs):
            if verbosity == 1:
                print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
                print(func(*args, kwargs))
            if verbosity > 1:
                print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
                print(func(*args, kwargs))
        return wrapper
    return decorator

@verbose_logger(verbosity=1)
def add(a,b):
    return a+b
# add(2,3)

@verbose_logger(verbosity=2)
def mul(a,b,c):
    return a*b*c
# mul(2,3,4)

# Decorators in Using Class
"""
You can define a decorator as a standalone function or as a method within a class. If it's a class 
method or static method decorator, it will need to handle the self or cls parameter appropriately.
"""

# Standalone Decorator Applied to Class Methods
import time

def log_method_call(method):
    def wrapper(self, *args, kwargs):
        print(f"Calling method {method.__name__} with arguments {args} and keyword arguments {kwargs}")
        start_time = time.time()
        result = method(self, *args, kwargs)
        end_time = time.time()
        print(f"Method {method.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Apply the Decorator in a Class
class math_calculation:
    @log_method_call
    def add(self,a,b):
        print(a+b)

        
    @log_method_call
    def mul(self,a,b,c):
        print(a*b*c)


"""
Standalone Decorator Function:
Define: Create a decorator function outside the class.
Apply: Use @decorator_name above the method definitions.

Class Method or Static Method Decorator:
Define: Create a decorator method inside the class, typically as a @staticmethod or @classmethod.
Apply: Use @log_method_call (or similar) directly above the method.

Decorator with Arguments:
Define: Create a decorator method that returns another decorator function, allowing you to pass arguments.
Apply: Use @decorator_name(arguments) above the method
"""

class MathOperations:
    @staticmethod
    def log_execution_time(verbosity=1):
        def decorator(method):
            def wrapper(self, *args, kwargs):
                if verbosity > 0:
                    print(f"Calling method {method.__name__} with arguments {args} and keyword arguments {kwargs}")
                start_time = time.time()
                result = method(self, *args, kwargs)
                end_time = time.time()
                if verbosity > 1:
                    print(f"Method {method.__name__} took {end_time - start_time:.4f} seconds")
                return result
            return wrapper
        return decorator

    @log_execution_time(verbosity=2)
    def add(self, a, b):
        time.sleep(1)  # Simulate a delay
        return a + b

    @log_execution_time(verbosity=1)
    def multiply(self, a, b):
        time.sleep(2)  # Simulate a delay
        return a * b

# Property Decorators
class PropertyDecorators:
    def __init__(self, value: int) -> None:
        self._value = value
    """
    Decorator Method Names:
    The setter and deleter decorators should be applied to methods with the same name as the property 
    method, not to methods with different names.
    
    Using '@property' Decorator:
    The '@property' decorator is used to define a method that will be accessed like an attribute.
    
    Using '@property_name.setter' and '@property_name.deleter':
    The setter and deleter decorators should be applied to methods that modify or delete the property, 
    and they must be named the same as the property defined with @property.
    """
    
    """
    @property: Turns a method into a read-only attribute.
    @property_name.setter: Defines a method for setting the property.
    @property_name.deleter: Defines a method for deleting the property.
    """
    
    @property
    def value(self) -> int:
        """Getter method for the property."""
        return self._value
    
    @value.setter
    def value(self, new_value: int) -> None:
        """Setter method for the property."""
        self._value = new_value
    
    @value.deleter
    def value(self) -> None:
        """Deleter method for the property."""
        del self._value

    
if __name__=="__main__":
    # #creating an instance for math_calculation class
    obj = math_calculation()
    # # Call the decorated methods
    # obj.add(2,3)
    # obj.mul(2,3,4)
    

    # # Create an instance for MathOperations class
    math_ops = MathOperations()
    # Call the decorated methods
    # print(math_ops.add(5, 10))
    # print(math_ops.multiply(5, 10))


    # # creating an Instance of Property decorators class
    objP = PropertyDecorators(10)
    print(objP.value)  # Accesses the property, prints: 10

    objP.value = 20     # Sets a new value using the setter
    print(objP.value)  # Accesses the property, prints: 20

    del objP.value      # Deletes the property
    try:
        print(objP.value)  # Raises AttributeError because the property is deleted
    except AttributeError as e:
        print(e)  # Output: 'PropertyDecorators' object has no attribute '_value'