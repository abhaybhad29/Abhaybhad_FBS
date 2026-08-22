#Python Program to Multiply All the Items in a Dictionary
def multipy_dictionary(dictionary):
    result = 1

    for value in dictionary.values():
        result = result * value

    return result

d = {
    "a":2,
    "b":3,
    "c":4,
    "d":5
}    
answer = multipy_dictionary(d)
print("Multiply all value :",answer)