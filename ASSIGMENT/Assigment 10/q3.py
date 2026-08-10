#Write a program to find the second largest element in the list.
def second_largest(lst):
    largest = lst[0]
    second = lst[0]

    for i in lst:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i

    return second


lst = [10, 25, 5, 40, 15]

print("Second largest =", second_largest(lst))