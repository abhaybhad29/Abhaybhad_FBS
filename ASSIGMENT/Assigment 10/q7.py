#Write a program to create a new list from existing list which contains cube of
#each number of list.
def cube_list(lst):
    new_list = []

    for i in lst:
        new_list.append(i ** 3)

    return new_list


lst = [1, 2, 3, 4, 5]

print("Original list =", lst)
print("Cube list =", cube_list(lst))