# Find the missing number in an array (using summation and xor operation)

#  Formula = sum of numbers / (count of natural number * count of natural number +1 / 2)

arr = [1,2,4,5,6,7]

# # Using normal
# sum = 0
# sum1 = 0

# for i in arr:
#     sum+=i

# for i1 in range(1,len(arr)+2):
#     sum1+=i1

# missing = sum1-sum

# print(missing)

# using summation

def missing_summation(a):
    n = a[-1]
    sum1=0
    total = n*(n+1)//2
    sum1 = sum(a)

    missing1 = total - sum1
    print(missing1)

missing_summation(arr)
