class Product:
    #Base class for all product types in the inventory.

    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock

    def calculate_value(self):
        #Abstract method to be implemented by derived classes.
        raise NotImplementedError("calculate_value() must be implemented by subclasses")

class SimpleProduct(Product):
    """Product with unit price for calculating total value."""

    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        """Calculates total value by multiplying quantity by unit price."""
        return self.quantity_in_stock * self.unit_price

class PerishableProduct(Product):
    #Product with expiry date for discounted value based on shelf life.

    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price
        self.expiry_date = expiry_date

    def calculate_value(self):
        #Calculates total value with a discount based on remaining shelf life
        from datetime import date  # Import for date calculations

        today = date.today()
        days_remaining = (self.expiry_date - today).days

        # Adjust discount based on remaining shelf life (replace with your logic)
        discount_rate = 0  # No discount by default
        if days_remaining < 30:
            discount_rate = 0.1  # 10% discount for items nearing expiry

        discounted_price = self.unit_price * (1 - discount_rate)
        return discounted_price * self.quantity_in_stock

class DigitalProduct(Product):
    #Product with a single price for total value.

    def __init__(self, product_id, name, quantity_in_stock, price):
        super().__init__(product_id, name, quantity_in_stock)
        self.price = price

    def calculate_value(self):
        #Calculates total value based on current price.
        return self.price * self.quantity_in_stock

def main():
#Prompt user for product details and demonstrate usage
    while True:
        product_type = input("Enter product type (simple, perishable, digital): ").lower()

        if product_type not in ("simple", "perishable", "digital"):
            print("Invalid product type. Please try again.")
            continue

        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity in stock: "))

        if product_type == "simple":
            unit_price = float(input("Enter unit price: "))
            product = SimpleProduct(product_id, name, quantity, unit_price)
        elif product_type == "perishable":
            try:
                expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
                expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid expiry date format. Please use YYYY-MM-DD.")
                continue
            unit_price = float(input("Enter unit price: "))
            product = PerishableProduct(product_id, name, quantity, unit_price, expiry_date)
        else:
            price = float(input("Enter price: "))
            product = DigitalProduct(product_id, name, quantity, price)

        total_value = product.calculate_value()
        print(f"\nProduct: {product.name} ({product.product_id})")
        print(f"Total value: ${total_value:.2f}")

        choice = input("\nDo you want to add another product? (y/n): ").lower()
        if choice != "y":
            break

if __name__ == "__main__":
    main()
