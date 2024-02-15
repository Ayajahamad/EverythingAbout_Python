# 1. Accept 2 Number And Print Greatest Between them ?

num1 = int(input("Enter your first  Number :: "))
num2 = int(input("Enter your second  Number :: "))

if num1>num2:
    print(f"{num1} is Greater then {num2}")
elif num2>num1:
    print(f"{num2} is greated then {num1}")
else:
    print(f"{num1} and {num2} Both are Equal")
