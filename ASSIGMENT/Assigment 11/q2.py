#Python Program to Merge Two Lists and Sort it
def merge_sort(list1, list2):
    new_list = list1 + list2
    new_list.sort()
    return new_list


list1 = [30, 10, 50]
list2 = [40, 20, 60]

result = merge_sort(list1, list2)

print("Merged and sorted list =", result)