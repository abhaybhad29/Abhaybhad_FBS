#Python Program to Concatenate Two Dictionaries Into One
def concatenate(dict1,dict2):
    dict1.update(dict2)
    return dict1
d1 = {"name":"Abhay","age":21}
d2 = {"city":"pune","Eduction":"BCA"}
result = concatenate(d1,d2)
print("Concatenate Dictionaries :",result)