# # For Loop, While loop, & Nested Loops 

# ## For Loop
# """
#     The for loop is used for iterating over a sequence (like a list, tuple, string, or range) and executing a 
#     block of code for each item in the sequence.
# """

# # lst = [10,20,30,40,50]

# # for i in lst:
# #     print(i)
# #-------------------------------------------- Eg
# ## For loop with range() function.

# # for i in range(5):
# #     print(i)


# ## While Loop
# """
#     The while loop repeatedly executes a block of code as long as a condition remains True.
# """

# # count = 0
# # while count<=5:
# #     print(count)
    
# #     count+=1
# #---------------------------------- Eg
# # While loop with else block

# # count = 0
# # while count<6:
# #     print(count)
# #     count+=1
# # else:
# #     print("Loop in Else block..!")


# ## Nested Loops
# """
#     Loops can be nested inside other loops. Each loop executes completely before the next iteration of the 
#     outer loop starts.
# """

# # for i in range(3):
# #     for j in range(2):
# #         print(f"i = {i} : j = {j}")


# ## Loop Control Statements
# """
#     Break : Exits the loop immediately, regardless of the loop’s condition.
#     Continue : Skips the rest of the code inside the loop for the current iteration and proceeds to the next iteration.
#     else : Can be used with both for and while loops. The else block is executed when the loop terminates normally (i.e., not via a break statement).
# """

# # Break
# for i in range(10):
#     if i==5:
#         break
#     print(i)
 

# # Continue
# for i in range(10):
#     if i%2 == 0:
#         continue
#     print(i)


# # Else
# for i in range(5):
#     print(i)
# else:
#     print("Loop in Else block..!")

#------------------------------------ Problems On loops-----------------------------------#

# # 1. Given a list of integers, write a Python function that counts how many times the number 7 appears in the list using a loop. numbers = [1, 7, 3, 7, 5, 7, 9]

# numbers = [1, 7, 3, 7, 5, 7, 9]

# def number_Counter(lst, num):
#     count = 0
#     for i in lst:
#         if i==num:
#             count+=1
#     return count

# print(number_Counter(numbers,7))


# # 2.Write a Python program that prints a right-angled triangle of stars (*) with a given number of rows. For example, if the number of rows is 4, the output should be:
# """
#     *
#     
#     *
#     
# """
# n = int(input("Enter the number of rows :: "))
# for i in range(1,n):
#     for j in range(i):
#         print('*',end='')
#     print()


"""
When looping through dictionaries, the key and corresponding value can be retrieved at the same time using
the items() method.
"""
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
    
"""
When looping through a sequence, the position index and corresponding value can be retrieved at the same time 
using the enumerate() function.
"""
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v);

"""
To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
"""
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

"""
To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the 
reversed() function.
"""
for i in reversed(range(1, 10, 2)):
    print(i)
    

"""
To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while 
leaving the source unaltered.
"""
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
    
print("sor : ", sorted(basket))

"""
Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a 
sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.
"""
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)