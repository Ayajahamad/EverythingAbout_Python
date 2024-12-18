"""       
### What is a Dictionary?
- Definition: A dictionary is an unordered, mutable, and indexed collection of key-value pairs.
- Syntax: `{key1: value1, key2: value2, ...}`

### Key Characteristics
1. Unordered: The items in a dictionary do not have a defined order. The order may change when new items are added.
2. Mutable: You can change the contents of a dictionary after it has been created (add, remove, or modify key-value pairs).
3. Indexed by Keys: Each value is accessed using its associated key, rather than a numerical index.

### Creating a Dictionary
You can create a dictionary using curly braces `{}` or the `dict()` constructor.
"""


# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
        
# print(users)

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
        
# print(active_users)

# # Dictionary Comprehensoin
lst = [1,2,3,4,5]
dict_comprehension = {k:k*2 for k in lst}
# print(dict_comprehension)


# Some Examples
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

{'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']

del tel['sape']
tel['irv'] = 4127

{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)

['jack', 'guido', 'irv']
sorted(tel)

['guido', 'irv', 'jack']

'guido' in tel

'jack' not in tel

# # The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# Looping Techniques
"""
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using 
the items() method.
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    # print(k, v)
    pass


class dictionary:
    # Using curly braces
    my_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }

    # Using the dict() constructor
    my_dict = dict(name='Alice', age=30, city='New York')
    
    # You can access the value associated with a specific key using square brackets [].
    print(my_dict['name'])  # Output: Alice

    # You can add a new key-value pair or update an existing one using the assignment operator.
    my_dict['num'] = 9148271051 # Adding new key-value
    my_dict['city'] = 'Mayanmar' # Updating city
    
    # You can remove items using the 'del' statement or the 'pop()' method.
    my_dict.pop('name') # using pop() method
    del my_dict['city'] # using 'del'
    print(my_dict)
    
    def dictionary_methods(self):
        my_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
        }
        ### Common Dictionary Methods
        # 1. keys(): Returns a view object displaying a list of all keys.
        my_dict.keys()  # Output: dict_keys(['name', 'country'])
   
        # 2. values(): Returns a view object displaying a list of all values.   
        my_dict.values()  # Output: dict_values(['Alice', 'USA'])
   
        # 3. items(): Returns a view object displaying a list of all key-value pairs.
        my_dict.items()  # Output: dict_items([('name', 'Alice'), ('country', 'USA')])
   
        # 4. get(key,default): Returns the value for a specified key. If the key does not exist, it returns `None` or a specified default value.
        my_dict.get('city', 'Not Found')  # Output: Not Found
   
        # 5. clear(): Removes all items from the dictionary.
        my_dict.clear()  # Now my_dict is empty
   

### Dictionary Comprehension
# You can create dictionaries in a concise way using dictionary comprehension.

squares = {x: x*2 for x in range(5)}  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(squares)

### Nested Dictionaries
# Dictionaries can contain other dictionaries, allowing for complex data structures.
nested_dict = {
    'person': {
        'name': 'Alice',
        'age': 30
    },
    'job': {
        'title': 'Engineer',
        'company': 'Tech Co.'
    }
}



my_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }
### Iterating Over Dictionaries
# You can iterate through keys, values, or key-value pairs using loops.
for key in my_dict:
    print(key, my_dict[key])  # Iterate through keys

for value in my_dict.values():  # Iterate through values
    print(value)

for key, value in my_dict.items():  # Iterate through key-value pairs
    print(key, value)


"""
Given a list of words, write a function that counts the frequency of each word and returns a dictionary 
where the keys are the words and the values are their frequencies. Additionally, provide a sorted list 
of words based on their frequency in descending order.
"""
lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
dic = {}
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i] = 1
    
print(dic)


# Marging
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {}
for k,v in dict1.items():
    dict3[k] =v
    
for k,v in dict2.items():
    if k in dict3:
        dict3[k]+= v
    else:
        dict3[k] = v
print(dict3)

# updating a Dictionary updatae()
# Initial dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Update dict1 with dict2
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
