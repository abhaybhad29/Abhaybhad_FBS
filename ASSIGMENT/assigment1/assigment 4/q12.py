#Write a program to check if given number is Armstrong number or not.(for 3 digit)
num = int(input("Enter the number : "))
temp = num 
sum = 0
while temp > 0 :
    digit = temp % 10 
    sum = sum + (digit **3)
    temp = temp // 10
if sum == num:
    print("Armstorng num :",num)
else:
    print("Not a Armstorng num :",num)    