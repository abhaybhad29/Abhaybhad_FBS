#Python Program to Find the Union of two Lists
# Python program to find the union of two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# Union of two lists
union_list = list(set(list1) | set(list2))

print("Union of the two lists:", union_list)