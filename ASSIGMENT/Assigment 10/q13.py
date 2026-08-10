#Write a program to print list after removing even numbers.
def remove_even(lst):
    new_list = []

    for i in lst:
        if i % 2 != 0:
            new_list.append(i)

    return new_list


lst = [10, 15, 20, 25, 30, 35]

print("Original list =", lst)
print("List after removing even numbers =", remove_even(lst))