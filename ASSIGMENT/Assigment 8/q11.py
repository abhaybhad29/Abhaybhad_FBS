#WAP to check if a given number is Armstrong number or not. For
#each task create separate functions.
def armstrong(n):
    original = n
    digits = len(str(n))
    sum = 0

    while n > 0:
        digit = n % 10
        sum = sum + digit ** digits
        n = n // 10

    if original == sum:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if armstrong(n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")