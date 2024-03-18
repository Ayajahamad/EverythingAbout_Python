# Write a Python program to count the Frequency of words appearing in a string

def freeq_words():
    str = input("Enter a string to count the freequency :: ")
    li = str.split()
    dict = {}

    for s in li:
        if s not in dict.keys():
            dict[s] = 1
        else:
            dict[s] = dict[s] + 1
    print(dict)

freeq_words()