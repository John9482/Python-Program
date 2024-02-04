#prompt user to enter time period
time=int(input("Enter Time period of service="))
#prompt user to enter salary income
salary=int(input("Enter Your Salary="))
if time >10:
    bonus=0.1 * salary
    net_salary=bonus + salary
    print("Bonus:", bonus)
    print("Net salary",net_salary)
elif time >=6 and time <=10:
    bonus=0.08 * salary
    net_salary=bonus + salary
    print("Bonus:", bonus)
    print("Net salary",net_salary)
elif time <=6:
    bonus=0.05 * salary
    net_salary=bonus + salary
    print("Bonus:", bonus)
    print("Net salary",net_salary)
    
    

    
