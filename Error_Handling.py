"""
    # Error Handling
    Python errors can be broadly categorized into several types, each with its own characteristics and common scenarios.
"""

class Error_Handling:
    # Syntax Errors
    def syntax_Error(self):
        print("Syntax Error :")
        print("Description: Occurs when Python cannot parse the code due to incorrect syntax.\nHandling: Syntax errors are detected at compile time and cannot be handled at runtime. They need to be fixed in the code")
        
    # IndentationError
    def indentation_Error(self):
        print("IndentationError :")
        print("Description: Occurs when code blocks are not indented consistently.\nHandling: Similar to SyntaxError, these need to be corrected in the code\n")
        
    # NameError
    def name_Error(self):
        print("NameError :")
        print("Description: Occurs when a variable or function name is not defined \nHandling: Use try-except blocks to catch undefined variable issues")
        
        try:
            print(n)
        except NameError as e:
            print(f"Error : {e}\n")
            
    # TypeError
    def type_Error(self):
        print("TypeError :")
        print("Description: Occurs when an operation is performed on an object of inappropriate type.\nHandling: Use try-except blocks to catch type-related issues.")

        try:
            c = 4+"a"
            print(c)
        except TypeError as e:
            print(f"Error: {e}\n")

    # ValueError
    def value_Error(self):
        print("ValueError :")
        print("Description: Occurs when a function receives an argument of the right type but inappropriate value.\nHandling: Use try-except blocks to catch value-related issues.")
        
        try:
            a = int("str")
            # print(a)
        except ValueError as e:
            print(f"Error : {e}\n")
            
    # IndexError
    def index_Error(self):
        print("IndexError :")
        print("Description: Occurs when an index is out of range for a list or other sequence.\nHandling: Use try-except blocks to catch index-related issues.")

        lst = [1,2,3,4]
        try:
            a = lst[5]
        except IndexError as e:
            print(f"Error : {e}\n")
            
    # KeyError
    def key_Error(self):
        print("KeyError :")
        print("Description: Occurs when trying to access a dictionary with a key that doesn't exist.\nHandling: Use try-except blocks or dict.get() to handle missing keys.")
        
        dict = {'a':23,'b':24}
        
        try:
            b = dict["c"]
        except KeyError as e:
            print(f"Error :{e}\n")
            
    # AttributeError
    def attribute_Error(self):
        print("AttributeError :")
        print("Description: Occurs when an invalid attribute reference is made on an object.\nHandling: Use try-except blocks to catch attribute-related issues.")

        num = 45
     
        try:
            num.append(2)
        except AttributeError as e:
            print(f"Error : {e}\n")
            
    # ZeroDivisionError
    def zero_devisionError(self):
        print("ZeroDivisionError :")
        print("Description: Occurs when there is an attempt to divide by zero.\nHandling: Use try-except blocks to catch division by zero errors.")

        try:
            a = 30/0
        except ZeroDivisionError as e:
            print(f"Error : {e}\n")
            
    # FileNotFoundError
    def file_notFound(self):
        print("FileNotFoundError :")
        print("Description: Occurs when trying to open a file that does not exist.\nHandling: Use try-except blocks to catch file-related errors.")
        
        try:
            with open("some.txt",'r') as file:
                content = file.read()
        except FileNotFoundError as e:
            print(f"Error : {e}\n")

    # ImportError
    def import_Error(self):
        print("ImportError :")
        print("Description: Occurs when an import statement fails to find the module or object.\nHandling: Use try-except blocks to catch import errors.")
        
        try:
            import nonexistent_module
        except ImportError as e:
            print(f"Error : {e}\n")
    # OverflowError
    def overflow_Error(self):
        print("OverflowError :")
        print(f"Description: Occurs when a calculation exceeds the limits of the data type.\nHandling: Use try-except blocks to catch overflow errors.")

        import math
        try:
            result = math.factorial(10000)
            print(result)
        except Exception as e:
            print(f"Handled OverflowError: {e}\n")

    # Exception
    def exception_Error(self):
        print("Exception :")
        print("Description: An exception is an event that disrupts the normal flow of a program's execution. When an error occurs, Python generates an exception, which can be caught and handled using a set of predefined constructs to prevent the program from crashing")
        print("Handling: Use try-except blocks to catch Exceptional errors.")
        try:
            num = 30/0
        except Exception as e:
            print(f"Unexcepted Exceptional Error : {e}\n")
            
    # Multiple Errors handling
    def multiple_Errors(self):
        import math
        print("Multiple Errors Handling :")
        try:
            result = math.factorial(10000)
            print(result)
        except (OverflowError, MemoryError) as e:
            print(f"Error : {e}\n")
        except Exception as e:
            print(f"Error : {e}\n")


if __name__=='__main__':
    obj = Error_Handling()
    
    obj.syntax_Error()
    obj.indentation_Error()
    obj.name_Error()
    obj.type_Error()
    obj.value_Error()
    obj.index_Error()
    obj.key_Error()
    obj.attribute_Error()
    obj.zero_devisionError()
    obj.file_notFound()
    obj.import_Error()
    obj.exception_Error()
    obj.overflow_Error()
    obj.multiple_Errors()