from datetime import datetime

currentYear = datetime.now().year
currentMonth = datetime.now().month

print("currentYear : ", currentYear)
print("currentMonth : ", currentMonth)

for i in range(1, currentMonth + 1):
    print(i)
