## Explicit type coersiion/type casting

#1 - int(x): Converts x to an integer.
x = 10.5
integer_x = int(x)  # integer_x will be 10

#2 -  float(x): Converts x to a floating-point number.
x = 10
float_x = float(x)  # float_x will be 10.0

#3 - str(x): Converts x to a string.
x = 10
string_x = str(x)  # string_x will be '10'

#4 - list(x): Converts x to a list.
x = (1, 2, 3)  # tuple
list_x = list(x)  # list_x will be [1, 2, 3]

#5 - tuple(x): Converts x to a tuple.
x = [1, 2, 3]  # list
tuple_x = tuple(x)  # tuple_x will be (1, 2, 3)

#6 - set(x): Converts x to a set.
x = [1, 2, 2, 3, 3]  # list
set_x = set(x)  # set_x will be {1, 2, 3}

#7 - dict(x): Converts x to a dictionary. x should be an iterable of key-value pairs.
x = [('a', 1), ('b', 2)]  # list of tuples
dict_x = dict(x)  # dict_x will be {'a': 1, 'b': 2}

#8 - bool(x): Converts x to a Boolean value.
x = 10
bool_x = bool(x)  # bool_x will be True
