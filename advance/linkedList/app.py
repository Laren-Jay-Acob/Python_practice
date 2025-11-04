# Linked List Example

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = Node()
        
    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        print (f"Appended {data} to the linked list.")
    def display(self):
        elems = []
        curr = self.head
        while curr.next is not None:
            curr = curr.next
            elems.append(curr.data)
        print("Linked List contents:", elems)

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.display()