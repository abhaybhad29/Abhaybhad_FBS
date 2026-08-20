#Python Program to replace every blank space with hyphen in a string. using function
def replaceSpace(string):
    result = ''
    for ch in string:
        if ch == " ":
            result = result + '-'
        else:
            result = result + ch
    return result
str1 = input("Enter a string : ")
str2 = replaceSpace(str1)

print("String after replacing space :",str2)
