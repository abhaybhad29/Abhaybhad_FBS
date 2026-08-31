#5. Python Program to Find the Union of two Lists without
#using set concept.

def union_list(list1, list2):
    result = []

    for x in list1:
        if x not in result:
            result.append(x)

    for x in list2:
        if x not in result:
            result.append(x)

    return result


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = union_list(list1, list2)

print("Union =", result)

