#WAP to print Armstrong number within a given range
start = int(input("Enter the Starting number : "))
End = int(input("Enter the Ending number : "))
for num in range(start,End+1):
    temp = num
    sum = 0
    while temp >0:
        digits = temp % 10
        sum = sum + digits **3
        temp = temp // 10
    if num ==sum:
        print(num)    