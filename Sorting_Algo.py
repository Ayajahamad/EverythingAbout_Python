
arr = [3,4,2,7,5,9,1]
l = len(arr)
# print(l)

# # Bubble sort
# for i in range(l):
#     for j in range(0,l-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]           
# print(arr)


# # Selection sort
for i in range(l):
    min_ind = i
    for j in range(i+1,l):
        if arr[j] < arr[min_ind]:
            min_ind = j
            arr[i],arr[min_ind]=arr[min_ind],arr[i]  

print(arr)