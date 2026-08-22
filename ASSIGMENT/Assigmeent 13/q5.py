#Python Program to Sum All the Items in a Dictionary
def sum_dictionary(dictionary):
    total = 0

    for value in dictionary.values():
        total = total + value

    return total 

d = {
    "a":10,
    "b":20,
    "c":30,
    "d":40
} 
result = sum_dictionary(d)
print("Sum of dictionary :",result)
