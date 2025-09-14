# Definition of a Node in a singly linked list
class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data   
        self.next = None

head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

# length of Linked List
def length(head):
    length = 0
    curr = head
    
    while curr is not None:
        length += 1
        curr = curr.next
    return length 
def insert(head,new_element):
    new_node = Node(new_element)
    #new_node.next = head
    while head.next != None:
        head = head.next
    head.next = new_node
    return head
def print_linked_list(head):
    array = []
    curr = head
    
    while curr is not None:
        array.append(curr.data)
        curr = curr.next
    return array

insert(head,9) #* Initially it was head = insert(head,9). This hould not be the case as it will redefine the last list operations
print(print_linked_list(head))