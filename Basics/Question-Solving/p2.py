# 2. Accept the gender from the user, and print the respective greeting Message.
    #eg- Good mornig Sir or Madam

gender = input("Enter your Gender here F or M :: ")

if gender=="F" or gender=="f":
    print("Hlo dear Mam good morning..!")
elif gender=="M" or gender=="m":
    print("Hlo dear Sir good morning..!")
else:
    print("Please Enter the correct Gender..")