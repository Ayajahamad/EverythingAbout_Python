# Stack - LIFO: Last In First Out
"""
=> Basic operations we can do on a stack are:

Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top element on the stack.
isEmpty: Checks if the stack is empty.
Size: Finds the number of elements in the stack
"""

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
        return self.stack

    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


print(stack.pop())
print(stack.isEmpty())
print(stack.peek())
print(stack.size())



