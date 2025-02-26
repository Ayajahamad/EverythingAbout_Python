# Quick Sort: Chooses a pivot, partitions the array around it, then recursively sorts left and right.

def quick_sort(lst):
    if len(lst) < 1:
        return lst
        
    pivot = lst[len(lst) // 2]

    left = [i for i in lst if i < pivot]
    mid = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    
    return quick_sort(left) + mid + quick_sort(right)

lst = [2,4,5,6,3,1,1,9]
print(quick_sort(lst))