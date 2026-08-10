#Write a program to create a duplicate of an existing list. It should not point to
#same list.
def duplicate_list(lst):
    new_list = lst.copy()
    return new_list


lst = [10, 20, 30, 40, 50]

new_lst = duplicate_list(lst)

print("Original list =", lst)
print("Duplicate list =", new_lst)

# Change duplicate list
new_lst.append(60)

print("After modification:")
print("Original list =", lst)
print("Duplicate list =", new_lst)