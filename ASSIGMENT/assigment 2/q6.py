B_S = float(input("Enter the basic salary : "))


DA = (B_S * 10)/100
TA = (B_S * 12)/100
HRA = (B_S * 15)/100

Total_salary = B_S + DA + TA + HRA

print("DA=",DA)
print("TA=",TA)
print("HRA=",HRA)

print("The total salary is =",Total_salary)