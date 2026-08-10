num = int(input("enter the num : "))
if(num >1):
 for i in range (2 , num // 2 + 1):  # optimazition
    print(i)
    if(num % i == 0):
        print(f'{ num} is not prime number .')
        break
 else:
    print('num is prime number.')
else:
   print("num is not prime num .")
   
   