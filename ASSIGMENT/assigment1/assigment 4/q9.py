#WAP to print all numbers in a range divisible by a given number.
s = int(input("Enter the start number : "))
E = int(input("Enter the End number : "))
n = int(input("Enter the number : "))
for i in range(s , E +1):
    if i % n ==0:
        print(i)