#1.sturucture : Denoted by []
li =[10,20,30,40]
print(type(li))
#2.type of data :heterogeneous
li = [10,3.14,'abc']
print(li)

#3.sequece:ordered

#4.changable:
print(id(li))
li[1] =17.65
print(id(li))
print(li)

#5.duplication:
li = [10,10,20,30,20,10]
print(li)