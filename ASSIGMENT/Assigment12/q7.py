#Python Program to Calculate the Length of a String Without Using a
#Library Function
def string_length(s):
    count = 0

    for ch in s:
        count += 1

    return count


string = input("Enter a string: ")

print("Length of string:", string_length(string))