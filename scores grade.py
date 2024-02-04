print("Enter marks for three subjects")
subject_m=int(input("Enter marks for subject 1:"))
subject_e=int(input("Enter marks for subject 2:"))
subject_p=int(input("Enter marks for subject 3:"))
total=subject_m + subject_e + subject_p
average=total/3
print("Your average score is:",average)
if average >= 70 and average <=100:
    print("GRADE A")
elif  average >= 60 and average <=69:
    print("GRADE B")
elif  average >= 50 and average <=59:
    print("GRADE C")
elif  average >= 40 and average <=49:
    print("GRADE D")
elif  average >=0 and average <=39:
    print("FAIL")
