# Creating a singly LinkedList in Python,
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
node1 = Node(3)
node2 = Node(7)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1

print(currentNode)

while currentNode:
    print(currentNode.data, end=' -> ')
    currentNode = currentNode.next
    
print("null")