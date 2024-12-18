# '''
# The '->' symbol in Python is used in function annotations to indicate the return type of a function. 
# It’s part of Python's type hinting system, which allows you to specify the type of value a function is 
# expected to return. This can help with code readability and debugging, and it integrates with static 
# type checkers like mypy to catch type-related errors before runtime.

# # Function Annotations
# Function annotations provide a way to attach metadata to function arguments and return values. 
# Here’s a breakdown of how the -> symbol is used and how it works.

# #Syntax
# def function_name(parameter:type,parameter:type) -> return_type:
#     # Function body
#     pass
    
# # Parameters: These can be annotated with types using the 'parameter_name: type syntax'.
# # Return Type: The '-> return_type' syntax specifies what type of value the function is expected to return.
# '''


def add(a:int,b:int)->int:
    return a+b

# print(add(1,1))
   

def concatenate_strings(s1: str, s2: str) -> str:
    return s1 + s2

# print(concatenate_strings('hello','word.!'))

# Annotations are stored in the __annotations__ attribute of the function. You can access them like this:
def multiply(x: float, y: float) -> float:
    return x * y

# print(multiply.__annotations__)

# """
# Type Hinting: Type hints are optional in Python. They don’t enforce type checking at runtime but provide hints to developers and tools.
# Static Type Checkers: Tools like mypy can use these hints to check for type errors before runtime.
# No Runtime Enforcement: Python itself does not enforce type annotations. They are mainly for documentation and tooling purposes.
# """

from typing import List, Dict ,Tuple

def get_config(config: Dict[str, int]) -> int:
    return config['key']

# print(get_config({'key':12}))

# You can also use more complex types, such as lists, dictionaries, and tuples

def process_data(data: List[int], config: Dict[str, int]) -> Tuple[int, str]:
    return sum(data) , config.get('a', 0), 'Success'

# dictionary.get(key, default=None)

lst = [1,2,3]
dict = {'a':10,'b':20}
print(process_data(lst,dict))