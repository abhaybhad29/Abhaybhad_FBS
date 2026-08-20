#Python Program to count number of lowercase characters in a string.
def countLowercase(string):
    count = 0
    for ch in string:
        if "a" <= ch <="z":
            count +=1
    return count


str1 = input("Enter the string : ")
result = countLowercase(str1)
print("Result :",result)