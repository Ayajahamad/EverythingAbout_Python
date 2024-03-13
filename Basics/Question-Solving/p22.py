# 22. Find Whether Entered Number is Amstrong Or not.

n = input("Enter a number n :: ")
l = len(n)
num = 0
for i in n:
    num+= int(i)**l

if(num == n):
    print("The nUmber id Amstrong..")
else:
    print("Entered Number is not an Amstrong..")
