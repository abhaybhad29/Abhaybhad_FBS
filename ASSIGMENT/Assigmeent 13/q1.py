#Python Program to Add a Key-Value Pair to the Dictionary
student = {
    "name": "Abhay",
    "age": 21,
    "course":"BCA"
}
key = input("Enter key :")
value = input("Enter Value : ")
student[key] = value
print("Upload student details :",student)