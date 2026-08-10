num = int(input("Enter the three digits number : "))

unit = num % 10
tens = (num//10)%10
hundred = num // 100

Reverse_number = (unit*100) + (tens*10) + hundred
print("Reverse number is =", Reverse_number)