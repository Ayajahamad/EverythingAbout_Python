# 1. Given a sorted list and a number n, insert n into the list while maintaining the sorted order.

lst = [1,3,4,5,6,7,10]
n = 7
inserted = False
for i in range(len(lst)):
    if lst[i]>n:
        lst.insert(i,n)
        inserted = True
        break
if not inserted:
    lst.append(n)

print(lst)