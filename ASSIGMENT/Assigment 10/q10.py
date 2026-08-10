#Write a program to remove all occurrences of a given element in the list.
def remove_element(lst, n):
    new_list = []

    for i in lst:
        if i != n:
            new_list.append(i)

    return new_list


lst = [10, 20, 10, 30, 10, 40, 50]

n = int(input("Enter element to remove: "))

lst = remove_element(lst, n)

print("List after removing =", lst)