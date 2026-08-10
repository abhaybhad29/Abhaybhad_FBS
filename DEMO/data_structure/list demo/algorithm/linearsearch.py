def linearsearch (li,search_ele):
    for ind in range(0,len(li)):
        if(li[ind] == search_ele):
            return ind
    else:
        return -1

ele = int(input("enter ele to find: "))
li = [45,37,81,77,59,34,23,82]
res = linearsearch(li,ele)
if(res != -1):
    print(f'{ele} is present at index {res}. ')
else:
    print(f'{ele} is not present in list. ')            