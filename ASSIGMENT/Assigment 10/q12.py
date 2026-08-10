#Write a program to create three lists of numbers, their squares
#and cubes
def create_lists(n):
    numbers = []
    squares = []
    cubes = []

    for i in range(1, n + 1):
        numbers.append(i)
        squares.append(i ** 2)
        cubes.append(i ** 3)

    return numbers, squares, cubes


n = int(input("Enter n: "))

numbers, squares, cubes = create_lists(n)

print("Numbers =", numbers)
print("Squares =", squares)
print("Cubes =", cubes)