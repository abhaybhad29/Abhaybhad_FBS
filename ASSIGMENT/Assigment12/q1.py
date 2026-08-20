#Python Program to Replace all Occurrences of ‘a’ with $ in a String
def replace_a(s):
    result=""

    for ch in s:
        if ch == 'a':
            result +="$"
        else:
            result += ch

    return result

string = input("Enter string : ")
print("original string : ",string)  
print("New stringn :",replace_a(string))          