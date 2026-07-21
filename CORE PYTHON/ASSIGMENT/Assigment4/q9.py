#WAP to print all numbers in a range divisible by a given number.
n = int(input("Enter the number : "))
s = int(input("Enter the starting number : "))
e = int(input("Enter the end number : "))
for i in range(s,e+1):
    if i%n==0:
        print(i)