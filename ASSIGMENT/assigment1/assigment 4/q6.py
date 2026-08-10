#WAP to check if a given number is prime number or not.
n = int(input("Enter the num : "))
if(n >1):
    for i in range(2 , n // 2 +1):
        print(i)
    if(n % i == 0):
      print("num is not a prime num.")
    else:
       print("num is prime num.")  
else:
   print("num is not prime num.")       
