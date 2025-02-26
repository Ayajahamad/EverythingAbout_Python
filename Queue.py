# Queue - FIFO: First In First Out

"""
=> Basic operations we can do on a queue are:

Enqueue: Adds a new element to the queue.
Dequeue: Removes and returns the first (front) element from the queue.
Peek: Returns the first element in the queue.
isEmpty: Checks if the queue is empty.
Size: Finds the number of elements in the queue.
"""

class Queue:
    def __init__(self):
        self.queue = []
       
    def enqueue(self,ele):
        self.queue.append(ele)
        return self.queue
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return("Queue is Empty")
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        return("Queue is Empty")
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
   
queue = Queue()

# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)

print(queue.queue)

print(queue.dequeue())
print(queue.isEmpty())
print(queue.peek())
print(queue.size())