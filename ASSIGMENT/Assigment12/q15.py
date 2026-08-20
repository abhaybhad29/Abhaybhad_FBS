#Python Program to find larger string without using built-in functions.
def findLength(string):
    count = 0

    for ch in string:
        count += 1

    return count


def largerString(str1, str2):
    length1 = findLength(str1)
    length2 = findLength(str2)

    if length1 > length2:
        return str1
    elif length2 > length1:
        return str2
    else:
        return "Both strings are equal"


# Main program
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = largerString(str1, str2)

print("Larger string:", result)