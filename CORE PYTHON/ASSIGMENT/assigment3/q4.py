#Write a program to input all sides of a triangle and check whether triangle is valid or
#not.
a = int(input("Enter the 1st side of triangle :"))
b = int(input("Enter the 2nd side of triangle : "))
c = int(input("Enter the 3 rd side  of triangle :"))

if (a + b > c) and (a + c > b) and (b + c >a):
    print("The triangle is valid.")
else:
    print("The triangle is invalid.")