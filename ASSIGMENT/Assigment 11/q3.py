#Python Program to Sort the List According to the Second Element in Sublist
def sort_list(lst):
    lst.sort(key=lambda x: x[1])
    return lst


lst = [[1, 5], [2, 2], [3, 8], [4, 1]]

print("Original list =", lst)
print("Sorted list =", sort_list(lst))