# Write a python program to find out common letters between two strings

str1 = "NAINA"
str2 = "REENE"

unique1 = set(str1)
unique2 = set(str2)

common = unique1 & unique2
print(common)