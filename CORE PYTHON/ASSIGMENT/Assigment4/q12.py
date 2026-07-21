#Write a program to check if given number is Armstrong number or not.
num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")