#Python Program to Remove the nth Index Character from a Non-Empty
#String
def remove_nth_char(s, n):
    result = ""

    for i in range(len(s)):
        if i != n:
            result += s[i]

    return result


string = input("Enter a string: ")
n = int(input("Enter the index to remove: "))

print("Original String:", string)
print("New String:", remove_nth_char(string, n))