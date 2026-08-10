#Write a program to calculate area of rectangle using 
def area_rectangle(length, breadth):
    return length * breadth

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

area = area_rectangle(l, b)

print("Area of rectangle =", area)