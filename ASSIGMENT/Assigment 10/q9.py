#Write a program of having n number of elements in the list and find out even
#and odd elements in that list and then create two separate lists which will have
#even elements and other will have odd elements.
def separate_even_odd(lst):
    even = []
    odd = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd


n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

even, odd = separate_even_odd(lst)

print("Original list =", lst)
print("Even elements =", even)
print("Odd elements =", odd)