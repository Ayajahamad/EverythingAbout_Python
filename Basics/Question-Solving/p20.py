# 20. Print the Fibonacci series

n = int(input("Enter a number n :: "))

n1 = 0
n2 = 1
count = 2

if n < 0:
    print("Please Enter Positive Numbers")
elif n==0:
    print(n1)
else:
    while count<n:
        fib = n1+n2
        print(fib)
        count+=1
        n1 = n2
        n2 = fib
