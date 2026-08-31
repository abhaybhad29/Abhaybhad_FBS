#A list contains sublist with Emp information as follows :
#Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
#[210,”Tannu”,14000],[320,”Suresh”,35000]]
#Write a program to sort the list based on salary.

def sort_salary(data):
    data.sort(key=lambda x: x[2])
    return data


Data = [[101, "Seema", 45000],
        [340, "Rajani", 13000],
        [210, "Tannu", 14000],
        [320, "Suresh", 35000]]

result = sort_salary(Data)

print("Employees sorted by salary:")

for emp in result:
    print(emp)

