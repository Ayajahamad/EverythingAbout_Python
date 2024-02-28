# 16. Check Entered number is palindrome or Not.

n = int(input("Enter a number n :: "))
temp = n
rev = 0

while n>0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

if rev == temp:
    print("Entered Number is an Palindrome..")
else:
    print("Entered number is not a Palindrome..")