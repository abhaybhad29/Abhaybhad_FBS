#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.
n = int(input("Enter the number of pasenger : "))
cost = float(input("Enter the ticket cost : "))
total = 0
for i in range(n):
    age = int(input("Enter the age of passenger {i +1} : "))

    if age <12:
        ticket = cost -(cost *30/100)

    elif age < 59:
        ticket = cost -(cost * 50/100)

    else:
        ticket = cost 

    total = total + ticket

print("Total amount of ticket : ",total)               