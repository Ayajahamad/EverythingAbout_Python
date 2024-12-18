"""
    The key function for working with files in Python is the open() function.

    The open() function takes two parameters; filename, and mode.
    
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist.

    "a" - Append - Opens a file for appending, creates the file if it does not exist.

    "w" - Write - Opens a file for writing, creates the file if it does not exist.

    "x" - Create - Creates the specified file, returns an error if the file exists.
"""


# file = open("file_text.txt",'r')
# content = file.read()
# print(content)


# with open("file_text.txt", 'r') as file:
    
#     read = file.read()
#     print(f"read() method :\n{read}")
#     print(f"read() method :\n{read}")
    
    # read = file.readline()
    # print(f"readline() method :\n{read}")
    
    # read_lines = file.readlines()
    # print(f"readlines() method :\n{read_lines}")
    
    
    
with open("file_text.txt", 'w') as file:
    # file.write("New content Writed with file.write() method..!")
    
    file.writelines(["Line1\n LINE@\n line3\n"])
    



# # Opening a Non Existing file..
# with open("file_text1.txt",'w') as file:
#     file.write("Opened a Non Existing file with 'w' Mode..!")
    
with open("file_text.txt",'r') as file:
    content = file.read()
    print(content)