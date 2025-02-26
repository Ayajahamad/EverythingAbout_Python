# A basic circular doubly linked list in Python.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.prev = node4
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1

print("Moving Forward...")

current_node = node1
print(current_node.data, end=' -> ')
current_node = current_node.next
while current_node != node1:
    print(current_node.data, end=' -> ')
    current_node = current_node.next
print("(Back to Start)")

print("-------------------------------------")

print("Moving Backword...")
current_node = node4
print(current_node.data, end=' -> ')
current_node =  current_node.prev

while current_node!=node4:
    print(current_node.data, end=' -> ')
    current_node =  current_node.prev
print("(Back to End)")