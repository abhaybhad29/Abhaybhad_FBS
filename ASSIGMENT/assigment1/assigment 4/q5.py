#5.WAP to print Fibonacci series upto n.
#sum of previous 2 number
n = int(input("Enter the number "))
a = 0 
b = 1
for i in range(n):
    print(a, end = " ")
    c = a + b
    a = b
    b = c