def add_item(inventory, item, quantity):
    for i in range(len(inventory)):
        if inventory[i][0] == item:
            inventory[i] = (item, inventory[i][1] + quantity)
            return
    inventory.append((item, quantity))

def update_quantity(inventory, item, quantity):
    for i in range(len(inventory)):
        if inventory[i][0] == item:
            inventory[i] = (item, quantity)
            return
    print("Item not found in inventory.")

def get_item_quantity(inventory, item):
    for i in range(len(inventory)):
        if inventory[i][0] == item:
            return inventory[i][1]
    return 0

def calculate_total_quantity(inventory):
    total_quantity = 0
    for item, quantity in inventory:
        total_quantity += quantity
    return total_quantity

def main():
    inventory = []

    while True:
        print("\n1. Add item to inventory")
        print("2. Update item quantity")
        print("3. Get item quantity")
        print("4. Calculate total quantity")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(inventory, item, quantity)
            print("Item added to inventory.")

        elif choice == '2':
            item = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_quantity(inventory, item, quantity)
            print("Quantity updated.")

        elif choice == '3':
            item = input("Enter item name: ")
            quantity = get_item_quantity(inventory, item)
            print(f"Quantity of {item}: {quantity}")

        elif choice == '4':
            total_quantity = calculate_total_quantity(inventory)
            print(f"Total quantity of all items: {total_quantity}")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
