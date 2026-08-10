#Write a program to calculate simple interest based on Principal, Rate and Time
#(SI = P*R*T/100)
P = float(input("Enter the principle Amount : "))
R = float(input("Enter the Rate of interest : "))
T  = float(input("Enter the Time : "))
Si = (P*R*T)/100
print("Simple interest is : ",Si)