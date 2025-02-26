# Binary Search is much faster than Linear Search, but requires a sorted array to work.
"""
The Binary Search algorithm works by checking the value in the center of the array. If the 
target value is lower, the next value to check is in the center of the left half of the array. 
This way of searching means that the search area is always half of the previous search area, 
and this is why the Binary Search algorithm is so fast.
"""

def binary_Search(lst,n):
    low = 0
    high = len(lst)-1

    while low <= high:
        mid = (low+high)//2
        if lst[mid] == n:
            return mid
        elif lst[mid] > n:
            high = mid-1
        else :
            low = mid+1
    return -1
            
lst = [2,3,4,5,6,7,8,9]
n = 3
print(binary_Search(lst,n))