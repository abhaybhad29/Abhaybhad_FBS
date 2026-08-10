#Python Program to Find the Second Largest Number in a List Using Bubble
#Sort
def second_largest(lst):
    n = len(lst)

    # Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    # Find second largest
    for i in range(n - 2, -1, -1):
        if lst[i] != lst[n - 1]:
            return lst[i]


lst = [10, 25, 5, 40, 15, 30]

print("Original list =", lst)
print("Second largest =", second_largest(lst))