# 11. Factorial of a given Number.

fact = 1

n = int(input("Enter a number for Factorial :: "))

for i in range(1, n+1):
    fact*=i

print(fact)