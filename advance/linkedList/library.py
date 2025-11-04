# Library Using Linked List Implementation
class Node:
    def __init__ (self, data=None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__ (self):
        self.head = Node()
        
    def add_book(self, book_name):
        new_node = Node(book_name)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        print (f'Book "{book_name}" added to the library.')
    
    def delete_book(self, book_name):
        curr = self.head.next
        prev = self.head
        while curr is not None:
            if curr.data == book_name:
                prev.next = curr.next
                print (f'Book "{book_name}" deleted from the library.')
                return
            prev = curr
            curr = curr.next
        print (f'Book "{book_name}" not found in the library.')
        
    def display_books(self):
        elems = []
        curr = self.head.next
        while curr is not None:
            elems.append(curr.data)
            curr = curr.next
        print("Books in the library:")
        print('\n'.join(f'- {x}' for x in elems))
    
    def search_book(self, book_name):
        curr = self.head.next
        while curr is not None:
            if curr.data == book_name:
                print(f'Book "{book_name}" is available in the library.')
                return
            curr = curr.next
        print(f'Book "{book_name}" is not available in the library.')
        
if __name__ == "__main__":
    library = LinkedList()
    library.add_book("1984 by George Orwell")
    library.add_book("To Kill a Mockingbird by Harper Lee")
    library.add_book("The Great Gatsby by F. Scott Fitzgerald")
    library.add_book("1984 by George Orwell")
    library.add_book("To Kill a Mockingbird by Harper Lee")
    library.delete_book("The Great Gatsby by F. Scott Fitzgerald")
    library.display_books()