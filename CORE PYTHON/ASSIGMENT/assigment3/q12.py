num = int(input("Enter the number : "))
first = num // 100
last = num % 10
if first == last :
    print("The num is palindrome number.")
else:
    print("The num is not palindrome number.")