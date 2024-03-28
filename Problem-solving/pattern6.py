row = 6
for i in range(row):
    for j in range(row-i):
        print(" ",end=" ")
    for k in range(i+1):
        print('*',end=" ")
    print()

for i in range(row):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(row-i):
        print('*',end=" ")
    print()