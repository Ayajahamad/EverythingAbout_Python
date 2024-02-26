# 13. Find Entered number is perfect(strong) number or not.
 # ex - 6 first we need to find the factors of the number and, need to sum all factors excluding original number. 
 # if sum == original number - its an strong number else not.

n = int(input("Enter a number n :: "))

sum = 0
for i in range(1,n):
    if n%i == 0:
        sum+=i
if sum == n:
    print("Enetred Number is perfect Number..")
else:
    print("Enetred Number is not perfect Number..")