
## 1. Write a program that takes an integer input and prints whether the number is Positive, Negative or Zero.
  
# def check_Number(num):
#     if num<0:
#         print(f"Entered number: {num} is Negative")
#     elif num==0:
#         print(f"Entered number: {num} is Zero")
#     else:
#         print(f"Entered number: {num} is Positive")


# num = int(input("Enter a Number :: "))
# check_Number(num)



## 2. Write a program that takes 3 integer as input and prints the largest of the three numbers.
    
# def largest_Of_Three(inp1,inp2,inp3):
#     if inp1>inp2 and inp1>inp3:
#         print(f"The Integer {inp1} is Greater then {inp2} and {inp3}")
#     elif inp2>inp3 and inp2>inp1:
#         print(f"The Integer {inp2} is Greater then {inp2} and {inp3}")
#     else:
#         print(f"The Integer {inp3} is Greater then {inp1} and {inp2}")

# inp1 = int(input("Enter the First number :: "))
# inp2 = int(input("Enter the Second number :: "))
# inp3 = int(input("Enter the Third number :: "))

# largest_Of_Three(inp1,inp2,inp3)




## 3.Write a program that takes an integer input and prints whether the number is Even or Odd.

# def check_Even_or_Odd(num):
#     if num%2 == 0:
#         print(f"Entered Number {num} is Even..!")
#     else:
#         print(f"Entered Number {num} is odd..!")

# num = int(input("Eneter the Number :: "))
# check_Even_or_Odd(num)



## 4.Write a program that checks if a given year is leap yera or not.

# def leap_YearCheck(year):
#     if (year%4==0 and year%100!=0) or year%400==0:
#         print(f"The year {year} Is a leap year")
#     else:
#         print(f"The year {year} Is Not a leap year")
  
# year = int(input("Enter the year :: "))
# leap_YearCheck(year)



## 5.Write a program that checks if a Given string is Palindrome or not.

# def check_palindrome(inp):
#     rev = ""

#     for i in range(len(inp)-1,-1,-1):
#         rev+=inp[i]
 
#     if rev == inp:
#         print("Palindrome..!")
#     else:
#         print("Not a palindrome..!")
        
# inp = input("Enter a String : ")
# check_palindrome(inp)



## 6.Write a program that takes a student's marks as input and prints the corresponding grade based on the following criteria:
    # A(90-100),B(80-89),C(70-79),D(60-69),F(<60)

# def grade_Founder(marks):
#     if marks>=90 and marks<=100:
#         print(f"Student Total marks is {marks} and Grade is : A")
#     elif marks>=80 and marks<90:
#         print(f"Student Total marks is {marks} and Grade is : B")
#     elif marks>=70 and marks<80:
#         print(f"Student Total marks is {marks} and Grade is : C")
#     elif marks>=60 and marks<70:
#         print(f"Student Total marks is {marks} and Grade is : D")
#     elif marks<60:
#         print(f"Student Total marks is {marks} and Grade is : F")
#     else:
#         print("Invalid input..!")
        

# marks = int(input("Enter the total marks of a Student :: "))
# grade_Founder(marks)



## 7.Write a program that checks if a person is eligible to vote based on their age.

# def vote_Eligibility_Counter(age):
#     if age>=18:
#         print(f"Age of the person is {age} And He is Eligible for Vote..!")
#     elif age<18:
#         print(f"Age of the person is {age} And He is Not Eligible for Vote..!")
#     else:
#         print("Invalid input..!")
        
# age = int(input("Enter the Age :: "))
# vote_Eligibility_Counter(age)



## 8. Write a program that calculates a discount based on the purchase Amount If the purchase amont is 
    # above $100 , apply a 10% discount ; otherwise apply a 5% discount.

# def discount_Calculator(purchase_amount):
#     discount_rate_high = 0.10  # 10%
#     discount_rate_low = 0.05   # 5%

#     if purchase_amount>=100:
#         discount = purchase_amount*discount_rate_high
#         print(f"Purchase Amount is {purchase_amount} Discount Price {discount} Total is : {purchase_amount-discount}")
#     else:
#         discount = purchase_amount*discount_rate_low
#         print(f"Purchase Amount is {purchase_amount} Discount Price {discount} Total is : {purchase_amount-discount}")

# purchase_amount = int(input("Enter the Purchase Amount :: "))
# discount_Calculator(purchase_amount)



# 9.Write a program that checks if the given number is prime or not.

# def prime_Number(num):
#     count = 0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print(f"Entered number {num} is a Prime..!")
#     else:
#         print(f"Entered number {num} is not a prime..!")
 
# num = int(input("Enter the Number :: "))
# prime_Number(num)




## 10.Write a program that takes a number from 1 to 7 and prints the curresponding day of the week.

# def week_day_Founder(day):
#     match day:
#         case 1:
#             print(f"Week of the day {day} is Monday")
#         case 2:
#             print(f"Week of the day {day} is Tuesday")
#         case 3:
#             print(f"Week of the day {day} is Wednessday")
#         case 4:
#             print(f"Week of the day {day} is Thursday")
#         case 5:
#             print(f"Week of the day {day} is Friday")
#         case 6:
#             print(f"Week of the day {day} is Saturday")
#         case 7:
#             print(f"Week of the day {day} is Sunday")
#         case _:
#             print(f"Invalid Input..!")


# day = int(input("Enter the number of the Day :: "))
# week_day_Founder(day)


