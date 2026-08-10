#Write a program to remove duplicates from the list.
def remove_duplicates(lst):
    new_list = []

    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return new_list


lst = [10, 20, 10, 30, 20, 40, 10]

print("Original list =", lst)
print("List after removing duplicates =", remove_duplicates(lst))