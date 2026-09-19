print("======= SIMPLE CALCULATOR========")
num1 = float(input("Enter the number  one : "))
num2 = float(input("Enter the number two : "))
print("\nSelect oprator : ")
print("1.Addition (+)")
print("2. subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4) :")
if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    if num2 !=0:
        result = num1 / num2
    else:
        result = " Error! DIVISION BY ZERO." 
else:
    result = " Invaid choce!"

print("\nResult :",result)                           