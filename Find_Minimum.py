# 1. Finding Minimum Value in Array/List
lst = [2,4,5,1,0,9,8,7]
min_Val = lst[0]

for i in lst:
    if i < min_Val:
        min_Val = i
print("min_Value is :", min_Val)