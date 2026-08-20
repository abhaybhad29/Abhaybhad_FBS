#Python Program to Form a New String where the First Character and
#the Last Character have been Exchanged
def exchange_first_last(s):
    if len(s) <= 1:
        return s

    result = s[-1] + s[1:-1] + s[0]
    return result


string = input("Enter a string: ")

print("Original String:", string)
print("New String:", exchange_first_last(string))