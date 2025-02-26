# Singly Circular LinkedList.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Creating links
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

print("Singly Circular linked list..!")
curr_node = node1
start_node = node1
print(curr_node.data, end=" -> ")
curr_node = curr_node.next

while curr_node != start_node:
    print(curr_node.data, end=' -> ')
    curr_node = curr_node.next
    
print("Back to Start ...")
    