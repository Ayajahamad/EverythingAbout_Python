# 17. Find Whether entered number is an Strong Number or not.

n = int(input("Enter a number n :: "))

temp = n
num = 0

while n>0:
    a = n % 10
    fact = 1
    for i in range(1,a+1):
        fact*=i
    num += fact
    n = n // 10
if(num == temp):
    print(f"Entered Number {temp} is a Strong Number..")
else:
    print(f"Entered Number {temp} is not a Strong Number..")
