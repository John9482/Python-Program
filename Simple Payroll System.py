# Create class called Employee
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        raise NotImplementedError("This method must be overridden in a subclass")
# Create class called SalaryEmployee
class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
# Create class called HourlyEmployee
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate
# Create class called CommissionEmployee
class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission_value):
        super().__init__(emp_id, name, weekly_salary)
        self.commission_value = commission_value

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission_value
def main():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    employee_type = input("Enter employee type (Salary, Hourly, Commission): ")

    if employee_type.lower() == "salary":
        weekly_salary = float(input("Enter weekly salary: "))
        employee = SalaryEmployee(emp_id, name, weekly_salary)
    elif employee_type.lower() == "hourly":
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))
        employee = HourlyEmployee(emp_id, name, hours_worked, hourly_rate)
    elif employee_type.lower() == "commission":
        weekly_salary = float(input("Enter weekly salary: "))
        commission_value = float(input("Enter commission value: "))
        employee = CommissionEmployee(emp_id, name, weekly_salary, commission_value)
    else:
        print("Invalid employee type")
        return

    print(f"Weekly payroll for {employee.name} ({employee.emp_id}): {employee.calculate_payroll()}")

if __name__ == "__main__":
    main()
