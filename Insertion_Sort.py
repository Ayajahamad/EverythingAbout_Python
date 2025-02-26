# 1. Insertion Sort.
lst = [2,4,5,6,3,1,1]

n = len(lst)
for i in range(1,n):
    isert_index = i
    current_value = lst.pop(isert_index)
    
    for j in range(i-1,-1,-1):
        if lst[j] > current_value:
            isert_index = j
    lst.insert(isert_index,current_value)
        
print(lst)
