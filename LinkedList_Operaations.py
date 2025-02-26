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

# Traversing in LinkedList
def traversingLinkedList(head):
    current_node = head
    
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null") 
    
# Finding Lowest Value in LinkedList
def findLowest(head):
    min_value = head.data
    current_node = head
   
    while current_node:
        if current_node.data < min_value :
            min_value = current_node.data
        current_node = current_node.next
            
    print(min_value)
    
def deleteNode(head, nodetoDelete):
    if not head or not nodetoDelete:
        return head

    if head == nodetoDelete:
        return head.next

    current_node = head
    while current_node.next and current_node.next != nodetoDelete:
        current_node = current_node.next

    if current_node.next == nodetoDelete:
        current_node.next = nodetoDelete.next

    return head
    
if __name__ == "__main__":
    print("Linked List Traversing ...")
    traversingLinkedList(node1)
    
    print("Finding Minimun Value in LinkedList...")
    findLowest(node1)
    
    print("Deleting an Node in LinkedList...")
    deleteNode(node1, node3)
    traversingLinkedList(node1)