from datetime import datetime
#Create a function calculate_fine
def calculate_fine(bookID, dueDate, returnDate):
    # Converting  string dates to datetime objects
    due_date_obj = datetime.strptime(dueDate, "%Y-%m-%d")
    return_date_obj = datetime.strptime(returnDate, "%Y-%m-%d")
    
    # Calculate days _overdue
    days_overdue = (return_date_obj - due_date_obj).days
    
    # Determine fine_rate and fine_amount
    
    if days_overdue <= 7:
        fine_rate = 20
    elif days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100
    
    fine_amount = fine_rate * days_overdue
    
    print("Enter Book ID:", bookID)
    print("Due Date:", dueDate)
    print("Return Date:", returnDate)
    print("Days Overdue:", days_overdue)
    print("Fine Rate:", fine_rate)
    print("Fine Amount:", fine_amount)

bookID = input("Enter the  Book ID: ")
dueDate = input("Enter the  Due Date (YYYY-MM-DD): ")
returnDate = input("Enter the Return Date (YYYY-MM-DD): ")

calculate_fine(bookID, dueDate, returnDate)

