P = float(input("Enter the principle Amount : "))
R = float(input("Enter the Rate of interest : "))
T = float(input("Enter the Time(in month) : " ))

A = P*(1+R/100)**T

CI = A - P

print ("Amount =", A)
print ("compund interest =", CI)
