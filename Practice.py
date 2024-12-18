# The most useful form is to specify a 'default' value for one or more arguments. This creates a function that 
    # can be called with fewer arguments than it is defined to allow.

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
        
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 6)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')   


# The default values are evaluated at the point of function definition in the defining scope, so that
i = 5
def f(arg=i):
    print(arg) # will print 5.

i = 6
# f()

"""
 The default value is evaluated only once. This makes a difference when the default is a mutable object such 
 as a list, dictionary, or instances of most classes. For example, the following function accumulates the 
 arguments passed to it on subsequent calls:
"""
def f(a, L=[]):
    L.append(a)
    return L

# print(f(1))
# print(f(2))
# print(f(3))

# If you don't want the default to be shared between subsequent calls, you can write the function like this instead:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# Keyword Arguments
# Functions can also be called using keyword arguments of the form kwarg=value. For instance, the following function:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    
# accepts one required argument (voltage) and three optional arguments (state, action, and type). This function can be called in any of the following ways:

# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# -----------------------------------
# but all the following calls would be invalid:

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

# the positional arguments beyond the formal parameter list. (*name must occur before name.) For example, if we define a function like this:

def cheeseshop(kind, *arguments, keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        
# It could be called like this:
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# # Consider the following example function definitions paying close attention to the markers / and *:
# def standard_arg(arg):
#     print(arg)

# def pos_only_arg(arg, /):
#     print(arg)

# def kwd_only_arg(*, arg):
#     print(arg)

# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)
    
"""
Positional-only arguments (/): Must be specified by position; cannot be used as keywords.
Standard arguments: Can be specified by position or keyword.
Keyword-only arguments (*): Must be specified as keywords; cannot be passed positionally.
"""

# Lambda Expressions
"""
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two 
 arguments: lambda a, b: a+b. Lambda functions can be used wherever function objects are required. They are 
 syntactically restricted to a single expression.
 Semantically, they are just syntactic sugar for a normal function definition. Like nested function 
 definitions, lambda functions can reference variables from the containing scope
"""
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
f(1)


# Doc String in Python
"""
In Python, __doc__ is a special attribute that holds the documentation string (docstring) of a function, class,
or module. A docstring is a string that describes what the function (or class/module) does, and it's 
typically placed right below the function definition.
"""
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass
# calling function with doc string 
# print(my_function.__doc__)

"""
Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on 
any other part of the function. Parameter annotations are defined by a colon after the parameter name, followed
by an expression evaluating to the value of the annotation. Return annotations are defined by a 
literal ->, followed by an expression, between the parameter list and the colon denoting the end of the 
def statement. The following example has a required argument, an optional argument, and the return value annotated:
"""
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')