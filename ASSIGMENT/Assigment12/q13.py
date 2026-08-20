#Python Program to count number of digits and letters in a string.
def countdigitletter(string):
    digit = 0
    letter = 0

    for ch in string:
        if "0" <= ch <= "9":
            digit +=1
        elif("a"<= ch <= "z") or ("A"<= ch <= "z"):
            letter +=1

    return digit , letter 
str1 = input("Enter the string : ")
digit,letter = countdigitletter(str1)
print("Number of digit :",digit)
print("Number of letter :",letter)

       