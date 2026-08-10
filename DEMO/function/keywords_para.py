def emp(id,name,dept,sal):
    data = "ID :" + str(id) + '\n'
    data += "Name :" + str(name) + "\n"
    data += "Department :" + str(dept) + "\n"
    data +="Salary :" + str(sal) + "\n"
    return data
res = emp(name = "ABC", dept = "IT",sal =4000, id = 420)
print (res)