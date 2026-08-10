#Write a program to print all numbers which are divisible by m and n in the
#list.
def divisible(lst, m, n):
    for i in lst:
        if i % m == 0 and i % n == 0:
            print(i, end=" ")


lst = [10, 12, 15, 20, 24, 30, 40, 60]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("Numbers divisible by both m and n:")
divisible(lst, m, n)