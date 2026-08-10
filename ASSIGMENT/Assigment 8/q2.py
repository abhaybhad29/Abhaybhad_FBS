#Write a program to calculate area of circle
def area_circle(r):
    return 3.14 * r * r

r = float(input("Enter radius: "))

area = area_circle(r)

print("Area of circle =", area)