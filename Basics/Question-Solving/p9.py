# 9. Take a Number as an Input and print its Table.

num = int(input("Enter a number to Print a table :: "))

for i in range(1,11):
    print(f"{num} * {i} = {num*i}")