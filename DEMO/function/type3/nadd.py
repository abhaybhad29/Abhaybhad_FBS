#with passing parameter (with input)
#without returning value (without output)
def addition():
    num1 = int(input("Enter the num 1: "))
    num2 = int(input("Enter the num 2: "))

    sum = num1 + num2
    return  sum

res = addition()
print(res)