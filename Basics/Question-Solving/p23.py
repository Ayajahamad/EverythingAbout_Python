# 23. Find a Amstrong number in a Renge,

for n in range(1,1000):
    a = str(n)
    l = len(a)
    num = 0
    for i in a:
        num+= int(i)**l

    if(num == n):
        print(n)