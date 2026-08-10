#Write a program to print list after removing even numbers.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []

for i in list1:
    if i % 2 != 0:
        result.append(i)

print("List after removing even numbers:", result)