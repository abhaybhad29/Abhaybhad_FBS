def add(*num):
    sum = 0
    for val in num:
        sum +=val
    return sum
res = add(34,56,76)
print("Addition is : ",res)    
