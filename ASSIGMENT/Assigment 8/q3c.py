#c. 1^1 + 2^2 + 3^3+ ...... n^n
def sum_power(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i ** i

    return sum


n = int(input("Enter n: "))
print("Sum =", sum_power(n))