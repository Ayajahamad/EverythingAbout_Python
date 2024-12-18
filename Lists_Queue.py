"""
The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].
"""

# # Concept Of Queue in Python.
"""
A queue is a data structure that follows the First In, First Out (FIFO) principle, meaning that the first 
element added to the queue will be the first one to be removed. Queues are commonly used in scenarios where 
order needs to be preserved, such as in task scheduling, breadth-first search in graphs, and handling requests 
in a web server.

Key Operations of a Queue
Enqueue: Adding an element to the back of the queue.
Dequeue: Removing an element from the front of the queue.
Peek: Viewing the front element without removing it.
IsEmpty: Checking if the queue is empty.
"""

def que_Deque():
    from collections import deque

    queue = deque()
    queue.append(1)  # Enqueue
    queue.append(2)
    print(queue.popleft())  # Dequeue, Output: 1
    print(queue[0])         # Peek, Output: 2


def que_Queue():
    from queue import Queue

    queue = Queue()
    queue.put(1)  # Enqueue
    queue.put(2)
    print(queue.get())  # Dequeue, Output: 1
    print(queue.queue[0])  # Peek, Output: 2


# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]    

nested_List = [[row[i]*2 for row in matrix] for i in range(len(matrix))]
print(nested_List)