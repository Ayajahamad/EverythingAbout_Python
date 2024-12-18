# Built in classes define many magic methods, dir() function can show you magic methods inherited by a class.
# print(dir(int)) 


# Dunder methods are predefined methods that Python uses to perform operations on objects. 
    # For example, __add__ is called when you use the + operator with objects of a class. 
    # These methods help you customize how your objects behave with operators, functions, and built-in operations.
# Dunder methods are called when you use the (+,-,*) 'operator' with 'objects' of a class.


from audioop import add
from typing import Any


class Dunder_Methods():
    # magic method to initiate object
    def __init__(self,value):
        print("Initial method..!")
        self.value = value
        
    def __add__(self, other):
        return self.value + other +2
    
    def __sub__(self, other):
        return self.value - other
    
    def __call__(self, *args: Any, kwds: Any) -> Any:
        print("Hai",args)
        
    def __str__(self) -> str:
        return f"__str__ Method with value: {self.value}"
    
    def __repr__(self) -> str:
        # Return a string that could be used to recreate the object
        return f"Dunder_Methods({self.value!r})"

if __name__=='__main__':
    
    value1 = Dunder_Methods(7)
    # invoking __add__ method
    # __add__ is called when you use the + operator with 'objects' of a class.
    print(value1 + 4)
    
    # invoking __sub__ method
    print(value1 - 3)
    
    # invoking call() method
    value1(2,3,4)
    
    # invoking str() method
    # invoking __str__ method implicitly through print()
    print(value1)
    # invoking __str__ method explicitly using str()
    print(str(value1))
    
    # invoking __repr__ method
    print(repr(value1))
    
  