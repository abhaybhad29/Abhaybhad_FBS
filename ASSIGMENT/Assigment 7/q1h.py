n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(2 * (n - i)):
        print(" ", end=" ")

    for j in range(i, 0, -1):
        if i == 1 and j == 1:
            continue
        print(j, end=" ")

    print()
