# 1. Iterative Fibonacci Series – Uses a loop to generate the series.
n = 6

f= 0
s = 1
for i in range(0,n+1):
    t = f+s
    print(f)
    f = s
    s = t
    
# 2. Tail-Recursive Fibonacci Series with Global Counter – Uses recursion with a global counter to generate the series in a tail-recursive style.
n = 19

f= 0
s = 1
count = 0
def fib(f,s):
    global count
    if count <= n:
        new = f+s
        print(f)
        f = s
        s = new
        count+=1
        fib(f,s)
fib(f,s)    

# 3. Classic Recursive Fibonacci – Uses standard recursion to compute the nth Fibonacci number.
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
print(fib(6))
