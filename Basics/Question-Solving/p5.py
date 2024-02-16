# 5. Accept a Year and check leap or not

year = int(input("Enter a Age :: "))
if year % 4 == 0 and year % 100 != 0:
    print(f"The Entered Year {year} ia a Leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} in not an leap Year")