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
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))

            newItem = items.append((name, quantity, price))
            continue
        case 2: 
            for x in range(0, len(items)):
                print(f"Item: {x+1}. {items[x]}")
            continue
        case 3:
            totalCost = 0
            for i in items:
                totalCostPerItem = float(i[1]) * i[2]
                totalCost += totalCostPerItem
                
            print(f"Total Cost: {totalCost}")
            continue
        case 4:
            print("Exited")
            break
        case _:
            print("Invalid please choose between 1-4")
            continue

