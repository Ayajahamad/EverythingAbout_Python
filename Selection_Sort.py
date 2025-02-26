# 1. Selection Sort.
lst = [2,4,6,5,3,1,9]

n = len(lst)
for i in range(n-1):
    min = i
    for j in range(i+1,n):
        if lst[j] < lst[min]:
            min = j
    lst[i],lst[min] = lst[min],lst[i]
print(lst)