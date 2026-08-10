#Write a program to find the area and perimeter of following figure (Accept the
#length, breadth and radius from user:

l = float(input("Enter the lenght : "))
b = float(input("Enter the breadth : "))
r = float(input("Enter the radius"))
area =(l *b)+ (3.14 * r * r/2)
perimeter =(2 *l)+b+(3.14*r)
print("Area=",area)
print("Perimeter :",perimeter)