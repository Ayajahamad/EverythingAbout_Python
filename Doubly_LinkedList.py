# Doubly linked list.

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
node1 = Node(23)
node2 = Node(12)
node3 = Node(3)
node4 = Node(15)
node5 = Node(11)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node5

node5.prev = node4

print("Traversing Forward ->")
current_node = node1
while current_node:
    print(current_node.data, end=' -> ')
    current_node = current_node.next
print("null")

print("-------------------------------------")

print("Traversing Backword <-")
current_node = node5
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.prev
print("null")