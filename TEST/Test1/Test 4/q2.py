#Write a program to find factorial of given number using recursion
def facrotial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facrotial(n-1)
num = int(input("Enter a number:"))
print("Factorial of",num,"=",facrotial(num))    