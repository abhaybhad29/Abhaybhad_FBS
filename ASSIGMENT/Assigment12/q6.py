#Python Program to Take in a String and Replace Every Blank Space
#with Hyphen
def replace_space(s):
    result = ""

    for ch in s:
        if ch == " ":
            result += "-"
        else:
            result += ch

    return result


string = input("Enter a string: ")

print("Original String:", string)
print("New String:", replace_space(string))