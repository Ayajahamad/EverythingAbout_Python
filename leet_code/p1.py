l1 = [2,4,3]
l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807

map_l1 = list(map(int,str(int("".join(map(str, l1[::-1])))+int("".join(map(str, l2[::-1]))))))[::-1]


print(map_l1)