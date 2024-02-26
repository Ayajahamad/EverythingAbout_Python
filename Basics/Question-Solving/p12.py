# 12. Print all teh factors of the Number.

n = int(input("Enter a number To find the factors :: "))

for i in range(1,n+1):
    if n%i == 0:
        print(i, end=" ")