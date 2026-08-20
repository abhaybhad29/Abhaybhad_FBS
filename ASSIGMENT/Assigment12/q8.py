#Python Program to Remove the Characters of Odd Index Values in a
#String
def remove_odd_index(s):
    result = ""

    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i]

    return result


string = input("Enter a string: ")

print("Original String:", string)
print("New String:", remove_odd_index(string))
