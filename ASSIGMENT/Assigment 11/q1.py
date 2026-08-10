#Python Program to Put Even and Odd elements of a List into two Different
#Lists
def separate_even_odd(lst):
    even = []
    odd = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd


lst = [10, 15, 20, 25, 30, 35]

even, odd = separate_even_odd(lst)

print("Original list =", lst)
print("Even elements =", even)
print("Odd elements =", odd)