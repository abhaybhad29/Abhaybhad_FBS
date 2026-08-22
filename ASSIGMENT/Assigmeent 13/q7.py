#Python Program to Remove the Given Key from a Dictionary
def remove_key(dictionary , key):
    if key in dictionary:
        del dictionary[key]
        print("Key remove suffully.")
    else:
        print("key does not exits.")

student = {
    "name":"Abhay",
    "age":22,
    "course":"Bca",
    "city":"pune"

}   

key = input("Enter key to remove : ")
remove_key(student,key)
print("updated Dictionary:",student)