## Type coersion

## Implicit type conversion

#1. Arithmetic Operations:
a = 10 #integer
b = 2.3 #float
c = a+b # result will be converted implicitly to - float
print(c)

#2. Comparison Operations:
x = 10      # int
y = 10.0    # float
result = x == y   # Result will be True (int 10 is equal to float 10.0)

#3. String Concatenation:
x = 10      # int
y = " apples"
result = str(x) + y   # Result will be a string "10 apples"

#4. List Concatenation:
list1 = [1, 2, 3]   # list
list2 = [4, 5, 6]   # list
result = list1 + list2   # Result will be [1, 2, 3, 4, 5, 6]

#5. Membership Testing:
x = 3       # int
list1 = [1, 2, 3, 4, 5]   # list
result = x in list1   # Result will be True (3 is in the list)

#6. Logical Operations:
x = 10      # int
y = 5       # int
result = x > y and x == 10   # Result will be True



