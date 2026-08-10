#Write a program to find maximum and minimum element in a list.
def find_max_min(lst):
    maximum = lst[0]
    minimum = lst[0]

    for i in lst:
        if i > maximum:
            maximum = i

        if i < minimum:
            minimum = i

    return maximum, minimum


lst = [10, 25, 5, 40, 15]

maximum, minimum = find_max_min(lst)

print("Maximum =", maximum)
print("Minimum =", minimum)