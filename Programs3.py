# """
# 1.
# Given a list of words, write a function that counts the frequency of each word and returns a dictionary 
# where the keys are the words and the values are their frequencies. Additionally, provide a sorted list 
# of words based on their frequency in descending order.

# lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
# Dictionary: {'apple': 3, 'banana': 2, 'orange': 1}
# """

# dic = {}
# lst = ["apple", "banana", "apple", "orange", "banana", "apple"]

# for i in lst:
#    if i in dic:
#       dic[i]+=1
#    else:
#       dic[i] = 1
# # print(dic)      

# # Use sorted(my_dict.items()) to sort by keys.
# # Use sorted(my_dict.items(), key=lambda item: item[1]) to sort by values.
# # Add reverse=True for descending order

# sor = sorted(dic.items(),key=lambda i:i[1],reverse=True)
# # print(sor)

# # ---------Another Method
# lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
# d = {}
# for i in lst:
#     cpunt = 0
#     for j in lst:
#         if i==j:
#             cpunt+=1
            
#     d.update({i:cpunt})
# print(d)

# """
# 2. 
# You are given two dictionaries that contain the scores of students in two different subjects. Write a function that merges these dictionaries such that:
# -If a student appears in both dictionaries, their scores are summed.
# -If a student appears in only one dictionary, their score remains unchanged.

# math_scores = {'Alice': 90, 'Bob': 80}
# science_scores = {'Alice': 85, 'Charlie': 70}
# {
#     'Alice': 175,
#     'Bob': 80,
#     'Charlie': 70
# }
# """
# math_scores = {'Alice': 90, 'Bob': 80}
# science_scores = {'Alice': 85, 'Charlie': 70}
# n_dic= {}

# for k,v in math_scores.items():
#    if k in n_dic:
#       n_dic[k]+=v
#    else:
#       n_dic[k] =  v
      
# for k,v in science_scores.items():
#    if k in n_dic:
#       n_dic[k]+=v
#    else:
#       n_dic[k] =  v
      
# # print(n_dic)

# """
# 3.
# Write a function that takes a list of words and groups them by their lengths. Return a dictionary where 
# the keys are the lengths of the words, and the values are lists of words of that length.
# words = ["cat", "dog", "elephant", "fish", "bat"]
# # Expected Output: {3: ['cat', 'dog', 'bat'], 8: ['elephant']}
# """
# l_dict = {}
# words = ["cat", "dog", "elephant", "fish", "bat"]
# for i in words:
#    li = len(i)
#    if li not in l_dict:
#       l_dict[li] = []
#    l_dict[li].append(i)
   
# # print(l_dict)

# """
# 4.
# Write a function that counts the frequency of vowels in a given string and returns a dictionary where 
# the keys are the vowels and the values are their counts.
# input_string = "Hello World"
# # Expected Output: {'e': 1, 'o': 2}
# """
# input_string = "Hello World"
# ovel ='aeiouAEIOU'
# sp = input_string.split(' ')

# dic_s = {}
# for i in input_string:
#    if i in ovel:
#       if i not in dic_s:
#          dic_s[i] = 1
#       else:
#          dic_s[i] += 1
         
# # print(dic_s)

# """
# 5.
# Finding Common Elements
# Statement: Write a function that takes two lists and returns a dictionary where the keys are the common 
# elements in both lists, and the values are the counts of those elements in each list.

# list1 = ["apple", "banana", "orange", "apple"]
# list2 = ["banana", "kiwi", "apple", "apple"]
# Expected Output: {'apple': (2, 2), 'banana': (1, 1)}
# """
# dic_c = {}
# list1 = ["apple", "banana", "orange", "apple"]
# list2 = ["banana", "kiwi", "apple", "apple"]

# c1 = {}
# c2 = {}

# for i in list1:
#    if i not in c1:
#       c1[i] = 1
#    else:
#       c1[i] += 1
      
# for i in list2:
#    if i not in c2:
#       c2[i] = 1
#    else:
#       c2[i] += 1
      
# # print(c1)
# # print(c2)

# for i in c1:
#    if i in c2:
#       dic_c[i] = (c1[i],c2[i])
# # print(dic_c)

# """
# 6.
# Write a function that merges two dictionaries into one. If a key exists in both dictionaries, the value 
# from the second dictionary should replace the value from the first.

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# Expected Output: {'a': 1, 'b': 3, 'c': 4}
# """
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# # # With update()
# # dict1.update(dict2)
# # print(dict1)

# # or without update()
# n_dict = {}
# for i in dict1:
#    if i not in n_dict:
#       n_dict[i] = dict1[i]
# for i in dict2:
#    if i not in n_dict:
#       n_dict[i] = dict2[i]
#    else:
#       n_dict[i] = dict2[i]
# # print(n_dict)  
    
# """
# 7.
# Write a function that converts a list of tuples into a dictionary. Each tuple will contain a key-value 
# pair.
# tuples = [('a', 1), ('b', 2), ('c', 3)]
# Expected Output: {'a': 1, 'b': 2, 'c': 3}
# """
# tup_dic = {}
# tuples = [('a', 1), ('b', 2), ('c', 3)]

# # print(dict(tuples))
   

# """
# 8.
# Write a function that checks whether a list contains any duplicate elements. Return True if duplicates 
# exist, and False otherwise.

# items = [1, 2, 3, 4, 5]
# Expected Output: False
# """
# items = [1, 2, 3, 4, 5, 2]
# l = []
# dup = False
# for i in range(len(items)):
#    if items[i] in l:
#       dup = True
#       break
#    else:
#       l.append(items[i])
# print(dup)

