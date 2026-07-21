#WAP to check if a given number is prime number or not.
n = int(input("Enter the number : "))
count = 0
for i in range(1,n+1):
    if n % i ==0:
        count = count + 1
if count == 2:
    print("Num is a prime num :",n)
else:
    print("Num is not prime num :",n)