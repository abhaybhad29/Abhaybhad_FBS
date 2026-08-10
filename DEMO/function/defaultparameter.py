#To make parameter optional
#Assign value to parameter in function defne
#If we pass value to default parameter if take passed value
#if we don't pass value to default parameter it takes default value
#flow from right to left("positional parameter access")

def emp(id,name,sal,dept= 'IT'):
    print("ID :",id)
    print('Name :',name)
    print('Salary :',sal)
    print('Department  :',dept )

emp(101,"om",500000,)
print("*********************") 
emp("210","sachin",600000)   