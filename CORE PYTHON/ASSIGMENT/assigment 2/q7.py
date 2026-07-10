num = float(input("Enter the three digit number : "))

unit = num % 10
tens = (num //10)% 10
hundred = num // 100

sum = unit + tens + hundred
print("Enter the sum of three digits =",sum)
