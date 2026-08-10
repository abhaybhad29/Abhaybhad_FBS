#Python Program to Sort a List According to the Length of the Elements
#within the list.
def sort_by_length(lst):
    lst.sort(key=len)
    return lst


lst = ["apple", "hi", "banana", "cat", "a"]

print("Original list =", lst)
print("Sorted list =", sort_by_length(lst))