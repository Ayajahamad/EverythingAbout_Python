# 15. Saperate each digit of a number and Print it On new Line. without converting to string.

n = int(input("Enter a number n :: "))

while n > 0:
    print(n%10)
    n = n//10
