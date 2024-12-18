class String_Concept:
    # """
    # String: A string is a sequence of characters used to represent text. In Python, strings are 
    # enclosed in quotes, and they can contain letters, digits, symbols, and whitespace.
   
    # Basic Characteristics of Strings:
    
    # Immutable:
    # Strings in Python are immutable, meaning once a string is created, it cannot be changed. Any 
    # operation that modifies a string will create a new string.
    
    # Sequence Type:
    # Strings are a sequence type, which means you can access individual characters by their position 
    # (index) and can perform slicing to extract substrings.
    
    # Enclosed in Quotes:
    # Strings can be enclosed in single quotes ('), double quotes ("), or triple quotes (''') for 
    # multi-line strings.
    
    # Escape Sequences: Used to include special characters in strings.
    # \n – Newline
    # \t – Tab
    # \\ – Backslash
    # \" – Double quote
    # \' – Single quote
    # """
    def creating_strings(self):
      # Using Single Quotes
      s1 = 'Hello, World!'
      print(s1)

      # Using Double Quotes
      s2 = "Hello, World!"
      print(s2)
      
      # Using Triple Quotes (for multi-line strings)
      s3 = '''This is a 
      multi-line string.'''
      print(s3)

    def accessing_characters(self):
        # Indexing: Access individual characters using indices (0-based index).
        s = "Python"
        first_char = s[0]  
        last_char = s[-1]  
        print(first_char) # 'P'
        print(last_char) # 'n'

        # Slicing: Extract substrings using slice notation.
        substring = s[1:4]  
        print(substring) # 'yth'
     
    def string_length(self):
        s = "Python"
        # Using 'len()'
        length = len(s)  # 6
        print(length)

    def string_methods(self):
      s = "Python"
      # 'str.upper()': Convert all characters to uppercase.
      s.upper()  # 'PYTHON'

      # 'str.lower()': Convert all characters to lowercase.
      s.lower()  # 'python'
      
      # 'str.capitalize()': Capitalizes the first character of the string and makes all other characters lowercase
      s1 = "hello world"
      s1.capitalize()  # Output: 'Hello world'


      # 'str.title()': Convert the first character of each word to uppercase.
      s.title()  # 'Python'

      # 'str.strip()': Remove whitespace from the beginning and end of the string.
      s = "  Hello, World!  "
      s.strip()  # 'Hello, World!'

      # 'str.replace(old, new)': Replace occurrences of a substring with another substring.
      s.replace('World', 'Python')  # 'Hello, Python!'

      # 'str.split(delimiter)': Split the string into a list of substrings based on the delimiter.
      s.split(',')  # ['Hello', ' World!']

      # 'str.join(iterable)': Join elements of an iterable into a single string.
      '-'.join(['2024', '09', '16'])  # '2024-09-16'

      # 'str.find(substring)': Find the first occurrence of a substring. Returns '-1' if not found.
      s.find('World')  # 7
      
      # Padding and Aligning:
      # Use str.ljust(), str.rjust(), and str.center() for alignment.
      left_padded = s.ljust(10, '*')  # 'Python'
      right_padded = s.rjust(10, '-')  # '----Python'
      centered = s.center(10, '=')     # '==Python=='



    def string_formatting(self):  
      name = "Alice"
      age = 30
      
      # Using '%' Operator
      # Old-style formatting:  
      formatted_string = "Name: %s, Age: %d" % (name, age)

      # Using 'str.format()'
      # Modern formatting:
      formatted_string = "Name: {}, Age: {}".format(name, age)

      # Using f-strings (Python 3.6+)
      # Formatted string literals:
      formatted_string = f"Name: {name}, Age: {age}"

      # String Interpolation
      # f-strings allow embedding expressions inside string literals, using curly braces '{}'. They are evaluated at runtime and formatted using the '__format__()' method.
      name = "Bob"
      score = 95
      message = f"{name} scored {score} points."

      # String Encoding and Decoding

      # Encoding: Convert a string to bytes.
      s = "Hello"
      encoded_bytes = s.encode('utf-8')

      # Decoding: Convert bytes back to a string.
      decoded_string = encoded_bytes.decode('utf-8')
  
      # Raw Strings-----------------
      # Raw strings ignore escape sequences. Useful for regular expressions or file paths.
      raw_string = r"C:\Users\Name"
      print("raw_string : ",raw_string)

      # String Immutability----------------
      # Strings in Python are 'immutable', meaning once created, their contents cannot be changed. Any operation that appears to modify a string actually creates a new string.
      s = "Hello"
      s = s + " World"  # Creates a new string, 'Hello World'

      # String Methods for Searching and Replacing---------------------
      # 'str.startswith(prefix)': Check if the string starts with the specified prefix.
      s.startswith('Hello')  # True

      # 'str.endswith(suffix)': Check if the string ends with the specified suffix.
      s.endswith('World')  # True

      # Common String Operation.------------------
      # Concatenation: Combine strings using the '+' operator.
      s1 = "Hello"
      s2 = "World"
      combined = s1 + " " + s2  # 'Hello World'

      # Repetition: Repeat strings using the '*' operator.
      repeated = "Hello" * 3  # 'HelloHelloHello'

      # String Traversal: Iterate over characters in a string.
      for char in "Python":
          print(char)


      # String Validation----------------------------
    def string_validation(self):
        # 'str.isdigit()': Check if all characters are digits.
        "123".isdigit()  # True

        # 'str.isalpha()': Check if all characters are alphabetic.
        "abc".isalpha()  # True
 
        # 'str.islower()': Check if all characters are lowercase.
        "python".islower()  # True

        # 'str.isupper()': Check if all characters are uppercase.
        "PYTHON".isupper()  # True

        # Example 1: String with only spaces
        s1 = "     "
        print(s1.isspace())  # Output: True

        # Example 2: String with spaces and tabs
        s2 = " \t \n "
        print(s2.isspace())  # Output: True

        # Example 3: String with letters
        s3 = "Python"
        print(s3.isspace())  # Output: False

        # Example 4: Empty string
        s4 = ""
        print(s4.isspace())  # Output: False

        # Example 5: String with mixed content
        s5 = "Python 2024"
        print(s5.isspace())  # Output: False

        # Example 6: String with whitespace and non-whitespace characters
        s6 = "  Python  "
        print(s6.isspace())  # Output: False

      
    def string_interning(self):
       # Interning: Python optimizes memory usage by storing only one copy of immutable strings with the same value.
       a = "hello"
       b = "hello"
       print(a is b)  # Output: True


"""
String : in Python are sequences of characters, immutable, and come with a rich set of methods for manipulation.
String operations : include creating, accessing, formatting, and manipulating strings.
Copying strings : involves understanding that they are immutable and any operation results in new strings rather than modifying existing ones.
String methods : help in tasks like searching, replacing, encoding, and formatting strings.
"""

if __name__=='__main__':
    obj = String_Concept()
    
    obj.creating_strings()
    
    obj.accessing_characters()
    
    obj.string_length()

    obj.string_formatting()
    
    obj.string_methods()
    
    obj.string_validation()
    
    obj.string_interning()
