#Write a program to check whether the triangle is equilateral, isosceles or scalene
#triangle.
a = int(input("Enter frist angle :"))
b = int(input("Enter second angle :"))
c = int(input("Enter third angle :"))

if (a + b > c) and (a + c > b) and (b + c >a):
    if a ==  b ==   c :
        print("The triangle is equilateral.")
    elif a ==b or b ==c or c ==a :
        print("The triangle is isoscalen .")
    else:
        print("The triangle is scalen.")
else:
    print("Triangle is invalid.")        