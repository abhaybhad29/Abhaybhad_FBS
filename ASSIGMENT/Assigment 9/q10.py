#Write a program to reverse a number using recursion.
def reverse(n, rev=0):
    if n == 0:
        return rev

    digit = n % 10
    rev = rev * 10 + digit

    return reverse(n // 10, rev)


n = int(input("Enter a number: "))

print("Reverse =", reverse(n))