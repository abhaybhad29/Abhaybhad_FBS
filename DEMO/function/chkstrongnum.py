def chkStrongnum(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def is_strong(num):
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total = total + chkStrongnum(digit)
        num = num // 10

    return total == original


n = int(input("Enter a number: "))

if is_strong(n):
    print("Strong Number")
else:
    print("Not a Strong Number")