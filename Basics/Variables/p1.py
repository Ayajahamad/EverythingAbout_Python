# Variable Declaration and Assignment
"""
This is a comment
written in
more than just one line
"""

x = 10
print(x)

name = "xyz"
print(name)

## Naming Rules
a = 10
A = 20
_a = "Starting with underScore"
a1 = "Variable with number"

print(a)
print(A)
print(_a)
print(a1)

## Variable Swaping
b = 10
c = 20

temp = b
b = c
c = temp

print(b)
print(c)

# Variable Declaration and Assignment
x = 5
name = "John"

# Variable Types
a = 10          # int
b = 3.14        # float
c = "hello"     # str
d = True        # bool
e = [1, 2, 3]   # list
f = (1, 2, 3)   # tuple
g = {'a': 1, 'b': 2}   # dict
h = {1, 2, 3}   # set

# Dynamic Typing
x = 5           # x is an integer
x = "hello"     # x is now a string

# Variable Scope
global_var = 10

def my_function():
    local_var = 20
    print(global_var)   # Accessing global variable

# Variable Reassignment and Mutation
my_list = [1, 2, 3]
my_list[0] = 10     # Mutation of list element
