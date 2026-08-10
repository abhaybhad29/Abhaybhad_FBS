def sum_factorial(n):
    fact = 1
    sum = 0

    for i in range(1, n + 1):
        fact = fact * i
        sum = sum + fact

    return sum


n = int(input("Enter n: "))
print("Sum =", sum_factorial(n))