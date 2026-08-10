#Write a program to reverse the list.
def reverse_list(lst):
    rev = []

    for i in range(len(lst) - 1, -1, -1):
        rev.append(lst[i])

    return rev


lst = [10, 20, 30, 40, 50]

print("Original list =", lst)
print("Reversed list =", reverse_list(lst))