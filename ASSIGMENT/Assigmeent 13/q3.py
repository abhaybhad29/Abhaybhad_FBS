#3. Python Program to Check if a Given Key Exists in a Dictionary or Not
def check_key(dictionary , key):
    if key in dictionary:
        print("Key Exists in a dictionary.")
    else:
        print("Key are not Exists in a dictionary.")
student = {
    "name":"Abhay",
    "Age": 21,
    "course":"BCA"

}
key = input("Enter key : ")
check_key(student,key)
            