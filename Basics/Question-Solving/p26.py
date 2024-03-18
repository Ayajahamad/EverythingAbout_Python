# Write a Python program to convert two dictionary in to dictionary.

def list_to_dict():
    keys = [1,2,3,4,5]
    value = ["one","two","three","four","five"]

    print(dict(zip(keys,value)))

    dic = dict(zip(keys,value))
    for k in dic:
        print(k , ":" , dic[k])

list_to_dict()