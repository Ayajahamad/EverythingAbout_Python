# The str() function is meant to return representations of values which are fairly human-readable, 
# while repr() is meant to generate representations which can be read by the interpreter.
import datetime

"""
Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), 
'!s' applies str(), and '!r' applies repr().
"""

s = 'Hello, world.'
str(s) # 'Hello, world.'
repr(s) # "'Hello, world.'"

class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __repr__(self):
      return f"Person('{self.name}', {self.age})"

obj = Person('abc',20 )
# print(obj)

# print(repr(obj))

# f-strings support = for self-documenting expressions and debugging
user = 'eric_idle'
member_since = datetime.date(1975, 7, 31)
f'{user=} {member_since=}'
# print("user='eric_idle' member_since=datetime.date(1975, 7, 31)")

"""
The standard module called json can take Python data hierarchies, and convert them to string 
representations; this process is called serializing. Reconstructing the data from the string 
representation is called deserializing.
Between serializing and deserializing, the string representing the object may have been stored in 
a file or data, or sent over a network connection to some distant machine.
"""
def serializing():
   import json
   x = [1, 'simple', 'list']
   S_data = json.dumps(x)
   # print(S_data)
# serializing()

"""
Serialization:
json.dumps(data): Converts the Python object data into a JSON-formatted string.
json.dump(data, file): Writes the JSON representation of the object directly to a file.

Deserialization:
json.loads(json_string): Converts a JSON string back into a Python object.
json.load(file): Reads JSON data from a file and converts it back into a Python object.
"""


