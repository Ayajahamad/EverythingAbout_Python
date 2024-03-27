# Inverted Right-angled Triangle Pattern
row = 6

for i in range(row):
    for j in range(row-i):
        print('*',end=' ')
    print()