#Given two sets of numbers, write a Python program to find the missing
#numbers in the second set as compared to the first and vice versa. Use the Python set.
def find_missing(set1, set2):
    missing_in_set2 = set1 - set2
    missing_in_set1 = set2 - set1

    print("Numbers missing in second set:", missing_in_set2)
    print("Numbers missing in first set:", missing_in_set1)


# Input
set1 = set(map(int, input("Enter numbers for first set: ").split()))
set2 = set(map(int, input("Enter numbers for second set: ").split()))

# Function call
find_missing(set1, set2)