# 18. Tell all the strong Number in a range

for n in range(1,1000000):
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
