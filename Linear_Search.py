# 1. Linear Search 

def linear_Search(lst,n):
    for i in range(len(lst)):
        if lst[i] == n:
            return i
    return -1
    
lst = [3,4,5,6,6,7,8,2,10]
print(linear_Search(lst,6))