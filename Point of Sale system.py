class SaleItem:
    def __init__(self, item_id, name, unit_price):
        self.item_id = item_id
        self.name = name
        self.unit_price = unit_price

    def calculate_total(self, quantity):
        pass  # Placeholder method, to be overridden by subclasses


class StandardItem(SaleItem):
    def calculate_total(self, quantity):
        return self.unit_price * quantity


class DiscountedItem(SaleItem):
    def __init__(self, item_id, name, unit_price, discount_percentage):
        super().__init__(item_id, name, unit_price)
        self.discount_percentage = discount_percentage

    def calculate_total(self, quantity):
        total_cost = self.unit_price * quantity
        discount_amount = total_cost * (self.discount_percentage / 100)
        return total_cost - discount_amount


class ServiceItem(SaleItem):
    def __init__(self, item_id, name, hourly_rate):
        super().__init__(item_id, name, hourly_rate)
        self.hourly_rate = hourly_rate

    def calculate_total(self, hours):
        return self.hourly_rate * hours


def main():
    # Prompt the user to choose an item type
    print("Choose item type:")
    print("1. Standard Item")
    print("2. Discounted Item")
    print("3. Service Item")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        unit_price = float(input("Enter unit price: "))
        quantity = int(input("Enter quantity: "))

        item = StandardItem(item_id, name, unit_price)
        total_cost = item.calculate_total(quantity)
        print("Total cost:", total_cost)

    elif choice == 2:
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        unit_price = float(input("Enter unit price: "))
        discount_percentage = float(input("Enter discount percentage: "))
        quantity = int(input("Enter quantity: "))

        item = DiscountedItem(item_id, name, unit_price, discount_percentage)
        total_cost = item.calculate_total(quantity)
        print("Total cost:", total_cost)

    elif choice == 3:
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        hourly_rate = float(input("Enter hourly rate: "))
        hours = float(input("Enter hours of service: "))

        item = ServiceItem(item_id, name, hourly_rate)
        total_cost = item.calculate_total(hours)
        print("Total cost:", total_cost)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
