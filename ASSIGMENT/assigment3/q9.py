#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
M = int(input("Enter the marks :"))
if (M > 80):
    print("Frist class.")
elif(M > 60):
    print("Second class.")
elif(M > 40):
    print("pass.")
else:
    print("Fail.")