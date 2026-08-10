def chkpallindrome():
    num = int(input("Enter the number : "))
    temp = num
    rev = 0

    while(temp >0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d

    if(num==rev):
            print("The Number is pallindrome .")
    else:
            print("The number is not pallindrome.")

chkpallindrome()
