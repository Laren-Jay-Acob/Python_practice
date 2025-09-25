movies = [
    {"title": "Inception", "price": 200, "seats": 5},
    {"title": "Interstellar", "price": 250, "seats": 3},
    {"title": "The Dark Knight", "price": 220, "seats": 4}
]

book = []

while True:
    print("Welcome to Movie Ticket Booking!")
    print("1. View Available Movies")
    print("2. Book a Ticket")
    print("3. View My Bookings")
    print("4. Exit\n")

    try:
        choice = int(input("Choose option:"))
    except ValueError:
        print("Please Choose from the following")
        continue
    
    match choice:
    
        case 1:
            print("\nAvailable Movies:")
            for i in range(0, len(movies)):
                print(f"{i+1}. {movies[i]["title"]} - {movies[i]["price"]} - {movies[i]["seats"]}")
            print("\n")
            continue

        case 2:
            try:
                movie_choice = int(input("Select movie number: "))
                quantity = int(input("How many Tickets? "))
            except ValueError:
                print("Invalid choice please enter a number")
                continue
            
            movie = movies[movie_choice - 1]

            book.append((movie_choice - 1, quantity, movie["price"]*quantity))
            print(f"✅ Booked {quantity} ticket(s) for {movie["title"]}. Total: {movie["price"]*quantity}")
            continue

        case 3:
            print("Your Bookings:")
            
            for i in book:
                print(f"- {i[0]} ({i[1]} tickets) - {i[2]}")
            continue
        
        case 4:
            break
        
        case _:
            print("Invalid Choice")
            continue
        