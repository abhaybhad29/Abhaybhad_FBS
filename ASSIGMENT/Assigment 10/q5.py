#Accept a number from user and check if this element is present in the list or
#not. Also tell how many times it is present in the list.
def search_element(lst, n):
    count = 0

    for i in lst:
        if i == n:
            count = count + 1

    if count > 0:
        print("Element is present")
        print("It is present", count, "times")
    else:
        print("Element is not present")


lst = [10, 20, 10, 30, 10, 40, 50]

n = int(input("Enter a number: "))

search_element(lst, n)