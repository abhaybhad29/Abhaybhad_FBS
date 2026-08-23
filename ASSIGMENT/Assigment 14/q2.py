#Write a Python program to remove the intersection of a second set
#with a first set.
def remove_intersection(set1,set2):
    set1.difference_update(set2)
    return set1

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

result = remove_intersection(set1,set2)
print("First set after removing intersection:",result)
