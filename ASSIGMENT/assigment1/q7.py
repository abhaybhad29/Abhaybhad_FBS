import math

a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))

#calculate descriment
d = b*b - 4 * a * c

#calculate the root
root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b + math.sqrt(d)) / (2*a)

print("Root1 =", root1)
print("Root2=",root2)