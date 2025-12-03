books = [] # list for books [title, author, year published]
members = [] # list for library members [studentID, name, course, year level]

# For Adding books function with borrowed default as false and borrower name default to " "
def addBooks(title, author, year_published, borrowed = False, borrower_name = ''):
    return books.append([title, author, year_published, borrowed, borrower_name])

# For Adding members function with id, name, course, year level
def addMembers(id, name, course, yearLevel):
    return members.append([id, name, course, yearLevel])

# Borrow Book Function
def handleBorrowBook(bookName, name):
    for book in books:
        # find the right book
        if bookName == book[0]:
            if not book[3]:  # check if not borrowed
                for member in members:
                    if name in member[1]:  # check if member exists
                        book[3] = True
                        book[4] = name
                        print(f"Book '{bookName}' successfully borrowed by {name}.")
                        print(books)
            else:
                print(f"Book '{bookName}' is already borrowed.")
            return  # stop after handling this book
    
    # if loop finishes with no return
    print(f"Book '{bookName}' not found.")

# returning book function            
def handleReturningBook(bookName):
    for book in books:
        if bookName not in book[0]:
            continue
        
    if book[3]:
      book[3] = False
      book[4] = ''  
      return

# function for removing books by name
def removeBook(bookName):
    for book in books:
        if bookName == book[0]:
            books.remove(book)
            print(f"Book {bookName} deleted.")
            return

# Function for deleting members using name
def removeMember(memberName):
    for member in members:
        if member_name == member[1]:
            members.remove(member)
            return

# Function for searching specific book
def searchSpecificBook(bookName):
    for book in books:
        if bookName not in book[0].lower(): # Converts to lower case to find similar name even with different capitalization
            print(f"Cannot find {bookName}")
            continue
        
        if bookName == book[0].lower():
            print(f"\tTitle: {book[0]}\tAuthor: {book[1]}\tYear Published: {book[2]}")
            return

while True:
    print("----------------------------------")
    print("Choose an Option")
    print("1. Add Books")
    print("2. Add Members")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Remove Books")
    print("6. Remove Members")
    print("7. View All Books")
    print("8. View All Members")
    print("9. View Borrowed Books")
    print("10. Search Specific Book")
    print("11. Exit")

    try:
        option = int(input("Enter option: "))
    except TypeError:
        print("Error please enter a number given in the option.")
    
    match option:
        case 1: # Add Books 
            # Enter Amount of books to add and title, author, and year publish check if the type is correct
            try:
                amount_book_to_add = int(input("\nHow many books you want to add?: "))
                
                for i in range(0, amount_book_to_add):
                    print(f"\nAdd book {i+1}/{amount_book_to_add}")
                    # Add Title, Author, Year Published
                    title = input("Enter title: ")
                    author = input("Enter author: ")
                    year_published = int(input("Enter year published: "))
                    
                    # Append title, author, year and borrwed as false
                    addBooks(title, author, year_published)
                continue
                    
            except TypeError:
                print("Please Enter Correct Input")
                continue
        case 2: # Add Member
            try:
                amount_member_to_add = int(input("\nHow many members you want to add?: "))

                for i in range(0, amount_member_to_add):
                    print(f"\nAdd Member {i+1}/{amount_member_to_add}")

                    # Input ID, Name, Course, Year Level
                    id = int(input("Enter ID: "))
                    name = input("Enter name: ")
                    course = input("Enter course: ").upper() # always uppercase
                    year_level = int(input("Enter year level: "))
                    
                    # append id, name, course, and year level
                    addMembers(id, name, course, year_level)
                continue
            
            except TypeError:
                print("Please enter a valid number")
                continue
                    
                    
            except TypeError:
                print("Please enter a valid number.")
                continue
        case 3: # Borrow Books
            try:
                amount_book_to_borrow = int(input("\nhow many books you want to borrow?: "))

                for i in range(0, amount_book_to_borrow):
                    book_name = input("Enter book name: ")
                    member_name = input("Enter member name: ")

                    handleBorrowBook(bookName=book_name, name=member_name)
                    print(f"{member_name} borrowed {book_name}.")
                continue
            except TypeError:
                print("Please enter a valid number.")
                continue
            
        case 4: # Returning book
            try:
                book_name = input("\nEnter book name to return: ")

                handleReturningBook(bookName=book_name)
                print(f"book {book_name} returned!")
                continue
            except TypeError:
                print("Please Enter a valid input.")
                continue
        case 5: # Remove Books in List
            try:
                amount_book_to_remove = int(input("\nhow many book you want to remove?: "))
            except TypeError:
                print("Please enter a valid input.")
                
            for i in range(0,amount_book_to_remove):
                    book_title = input("Enter book title to remove: ")
                    
                    removeBook(bookName=book_title)
                    continue
        case 6: # Remove Members in List
            try: # catch any type errors
                amount_member_to_remove = int(input("\nhow many members do you want to remove?: "))
            except:
                print("Please enter a valid input.")
                continue

            for i in range(0, amount_member_to_remove): 
                member_name = input("Enter member name to be deleted: ") # input member name
                
                # remove member using name
                removeMember(memberName=member_name)
                continue
        case 7: # Show all Book List
            if not books:
                print("No books in library.")
            for title, author, year_published, _, _ in books:
                print(f"\tTitle: {title}\tAuthor: {author}\tYear Published: {year_published}")
            continue
        case 8: # Show all Member List
            if not members:
                print("No member registered.")
            for id, name, course, year_level in members:
                print(f"\tID: {id}\tName: {name}\tCourse: {course}\tYear Level: {year_level}")
            continue
        case 9: # Show Borrowed Books
            for book in books:
                title = book[0]
                borrowed = book[3]
                borrower_name = book[4]

                if borrowed:
                    print(f"\tTitle: {title}\tMember: {borrower_name}")

        case 10: # Search Specific Book
            try:
                search_book = input("Enter Book Name: ").lower()

                searchSpecificBook(search_book)
                continue
            except TypeError:
                print("Please enter a valid input.")
                continue
        case 11:
            print("Ending Program, Goodbye!")
            break
        case _:
            print("Unknown Option Please Enter A Valid Option.")
            continue
