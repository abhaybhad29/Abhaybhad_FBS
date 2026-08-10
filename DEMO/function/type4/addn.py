#with passing parameter (with input)
#without returning value (without output)
def addition(num1,num2): #formal parameter / argument
    return num1 + num2
num1 = int(input("Enter the number1 :"))
num2 = int(input("Enter the number2 : "))
res = addition(num1,num2)

print("Addition ",res)