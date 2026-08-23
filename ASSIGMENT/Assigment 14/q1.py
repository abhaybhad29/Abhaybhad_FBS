#Write a Python program to find elements in a given set that are not in
#another set.
def find_difference(set1,set2):
    return set2 - set1

set1 = {1,2,3,4,5,6}
set2 ={3,4,5,6,7}

result =find_difference(set1,set2)
print("Difference :",result)