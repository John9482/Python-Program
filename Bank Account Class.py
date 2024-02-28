class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Account Opening:", self.date_of_opening)
        print("Balance:", self.balance)


# Prompting user for account details
account_number = input("Enter account number: ")
balance = float(input("Enter initial balance: "))
date_of_opening = input("Enter date of opening (YYYY-MM-DD): ")
customer_name = input("Enter customer name: ")

# Creating BankAccount object
account = BankAccount(account_number, balance, date_of_opening, customer_name)

# Testing methods
print("\n*** Initial Customer Details ***")
account.customer_details()

print("\n*** Deposit ***")
deposit_amount = float(input("Enter deposit amount: "))
print("Amount deposited:", account.deposit(deposit_amount))

print("\n*** Withdrawal ***")
withdraw_amount = float(input("Enter withdrawal amount: "))
print("Amount withdrawn:", account.withdraw(withdraw_amount))

print("\n*** Updated Customer Details ***")
account.customer_details()
