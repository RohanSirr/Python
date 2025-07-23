def showMenu():
    print("\n**** Shopping List Manager ****")
    print("1. Add item and quantity")
    print("2. View Shopping List")
    print("3. Update item quantity")
    print("4. Remove item(Purchased)")
    print("5. Sort List (A-Z or by quantity)")
    print("6. Exit")

def addItem(shoppingList):
    item = input("Enter item name: ").strip()
    qtyInput = input("Enter quantity: ").strip()
    if not qtyInput.isdigit() or int(qtyInput) <= 0:
        print("Please enter a positive integer for quantity")
        return
    qty = int(qtyInput)
    for entry in shoppingList:
        if entry['item'].lower() == item.lower():
            entry['quantity'] += qty
            print(f"Updated quantity of {item} to {entry['quantity']}.")
            return
    shoppingList.append({'item': item, 'quantity': qty})
    print("Item added to list.")

def viewItem(shoppingList):
    if not shoppingList:
        print("Shopping list is empty.")
    else:
        print("\n**** Shopping List ****")
        for idx, entry in enumerate(shoppingList, 1):
            print(f"{idx}. {entry['item']} - {entry['quantity']}")

def updateQuantity(shoppingList):
    viewItem(shoppingList)
    if not shoppingList:
        print("Shopping list is empty.")
        return
    num = input("Enter item number to update: ").strip()
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(shoppingList):
            newQty = input("Enter a new quantity: ")
            if newQty.isdigit() and int(newQty) > 0:
                shoppingList[idx]['quantity'] = int(newQty)
                print(f"Quantity of item {shoppingList[idx]['item']} updated to {shoppingList[idx]}")
            else:
                print("Invalid quantity. Please enter a positive integer.")
        else:
            print("Invalid item number. Please try again.")
    else:
        print("Invalid input. Please enter a number.")

def removeItem(shoppingList):
    viewItem(shoppingList)
    if not shoppingList:
        return
    num = input("Enter item number to remove: ").strip()
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(shoppingList):
            removed = shoppingList.pop(idx)
            print(f"Item {removed['item']} removed from list.")
        else:
            print("Invalid item number. Please try again.")
    else:
        print("Please enter a valid no. ")

def sortList(shoppingList):
    if not shoppingList:
        print("List is empty. Nothingg to sort.")
        return
    sortType = input("Sort by (1) Alphabet (2) Quantity ? Enter 1 or 2: ")
    if sortType == '1':
        shoppingList.sort(key=lambda x: x['item'].lower())
        print("Sorted Alphabetically A-Z")
    elif sortType == '2':
        shoppingList.sort(key=lambda x: int(x['quantity']))
        print("Sorted by Quantity")
    else:
        print("Invalid choice. Please try again.")

def main():
    shopping_list = []
    while True:
        showMenu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            addItem(shopping_list)
        elif choice == '2':
            viewItem(shopping_list)
        elif choice == '3':
            updateQuantity(shopping_list)
        elif choice == '4':
            removeItem(shopping_list)
        elif choice == '5':
            sortList(shopping_list)
        elif choice == '6':
            print("Exiting Shopping List Manager. Happy Shopping!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")

main()   
    

