rows = 6
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end='')
    for k in range(i+1):
        print('*',end=' ')
    print()

for i in range(rows):
    for j in range(i):
        print(' ', end="")
    for k in range(rows-i):
        print('*',end=' ')
    print()