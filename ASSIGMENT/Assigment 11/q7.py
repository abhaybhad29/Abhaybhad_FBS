#Python Program to Find the Intersection of Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = list(set(list1) & set(list2))

print("Intersection of two lists:", intersection)