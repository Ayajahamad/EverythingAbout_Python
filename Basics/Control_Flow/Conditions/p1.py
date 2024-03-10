## if statement

#EX1
num = 5
if (num < 10):
        print("Num is smaller than 10")

#Ex2
if ("Python" in ['Java', 'Python', 'C#'] ):
     print("true")

#Ex3
passing_Score = 60
my_Score = 67
if(my_Score >= passing_Score):
             print("Congratulations! You have passed your exam")

#Ex4 - if else Statement
num = 5
if(num > 10):
     print("number is greater than 10")
else:
     print("number is less than 10")

## Short hand if statement
i = 10
if i>0: print("Positive number")

## Short hand if-else statement
x = 10
print("positive") if x > 0 else print("nagative")

## multiple conditions in if statemant
num1 = 10
num2 = 20
num3 = 30

if (num1 == 10 and num2 == 20 and num3 == 10):
     print("All the conditions are true")
else:
	print("Some conditions are not matching")

## Ex
fruitName = "Apple"
if (fruitName == "Mango" or fruitName == "Apple" or fruitName == "Grapes"):
     print("It's a fruit")
   


