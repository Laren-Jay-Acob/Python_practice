items = [] # store items

while True:
    print("Welcome to Grocery CLI App")
    print("1. Add Item to cart")
    print("2. View Items")
    print("3. Get total cost")
    print("4. Exit")

    try:
        choice = int(input("Choose option: "))
    except ValueError:
        print("Invalid input please select a valid option")
        continue
        
    match choice:
        case 1: 
            name = input("Enter item name: ") # name of the product
            
            try:
                quantity = int(input("Enter quantity: ")) # quantity of the product
                price = float(input("Enter price per item: ")) # price per item
            except ValueError:
                print("Value must be a number") # Wrong Input
                continue

            items.append((name, quantity, price)) # Append to items in tuples format
            continue
        case 2: 
            if not items:
                print("no items on cart")
                continue
            
            for x in range(0, len(items)): # print item in range 0-items length 
                print(f"Item: {x+1}. {items[x]}")
            continue
        case 3:
            totalCost = 0 # total cost placeholder
            
            if not items:
                print("no items on cart")
                continue
            
            for i in items: # loop items
                totalCostPerItem = float(i[1]) * i[2] # multiply quantity per item
                totalCost += totalCostPerItem # Add total cost per item in total cost
                
            print(f"Total Cost: {totalCost}")
            continue
        case 4:
            print("Exited")
            break
        case _:
            print("Invalid please choose between 1-4")
            continue

