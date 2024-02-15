# 4. Accept the Name and Age from the user Check whether he is valid voter or Not.

name = input("Enter Your Name :: ")
age = int(input("Enter Your Age :: "))

if age>18:
    print(f"Hello {name} You are Valid Voter..")
elif age>0 and age<18:
    print(f"Hello {name} You are Invalid voter..")
else:
    print("Please Enter valid Age..")