#Write a program to input angles of a triangle and check whether triangle is valid or not.
A = int(input("Enter the 1 st Angle of triangle :"))
B = int(input("Enter the 2 nd Angle of triangle :"))
C = int(input("Enter te 3 rd angle of triangle :"))

if A + B + C == 180 :
    print("triangle is valid.")
else:
    print("triangle are invalid.")