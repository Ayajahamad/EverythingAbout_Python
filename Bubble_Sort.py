lst = [1,2,3,4,6,5]
comparison = 0

"""
1.
Name: "Naïve Bubble Sort"
Reason: It performs unnecessary comparisons because the inner loop always runs the full length, even when elements are already sorted.
"""
# for i in range(len(lst)):
#     for j in range(len(lst)-1):
#         comparison+=1
#         if lst[j]>lst[j+1]:
#             lst[j],lst[j+1] = lst[j+1],lst[j]
#             print(lst)
# print("Comparison : ", comparison)
      
"""
2.
Name: "Improved Bubble Sort"
Reason: The inner loop range decreases after each pass, reducing unnecessary comparisons.
"""
# n = len(lst)
# for i in range(n):
#     for j in range(n-i-1):
#         comparison+=1
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1],lst[j]
#             print(lst)
# print("Comparison : ", comparison)

"""
3.
Name: "Efficient Bubble Sort" or "Adaptive Bubble Sort"
Reason: It includes an early stopping mechanism (swap flag) to exit the loop when no swaps occur, improving performance on nearly sorted lists.
"""
n = len(lst)
for i in range(n):
    swapped = False
    for j in range(n - i - 1):
        print("j : ",j)
        comparison += 1
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            swapped = True
            print(lst)
    if not swapped:
        break
print("Comparison : ", comparison)

