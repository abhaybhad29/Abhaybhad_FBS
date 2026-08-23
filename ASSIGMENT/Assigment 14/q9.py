#Write a Python program to find all the unique combinations of 3
#numbers from a given list of numbers, adding up to a target number.
def find_combinations(number,target):
    result = []
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            for k in range(j+1,len(number)):
                if number[i] + number[j] + number[k] == target:
                    combination =(number[i],number[j],number[k])
                    if combination not in result:
                        result.append(combination)


    return result

numbers = [2 , 4 , 3, 5, 7, 8, 1]
target = 10
result = find_combinations(numbers,target)
print("Unique combination :")
for combination in  result:
    print(combination)                   