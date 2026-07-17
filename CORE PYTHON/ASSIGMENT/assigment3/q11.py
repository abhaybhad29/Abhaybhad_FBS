total = 0
#p1
age = int(input("Enter the age of p1 : "))
ticket = int(input("Enter the price of ticket : "))
if age < 12:
    amount = ticket - (ticket*30/100)

elif age > 59 :
    amount = ticket - (ticket * 50/100)
else:
    amount = ticket
    total = total + amount
#p2    
age = int(input("Enter the age of p2 : "))
ticket = int(input("Enter the price of ticket : "))
if age < 12:
    amount = ticket - (ticket*30/100)

elif age > 59 :
    amount = ticket - (ticket * 50/100)
else:
    amount = ticket
    total = total + amount
#p3
age = int(input("Enter the age of p3 : "))
ticket = int(input("Enter the price of ticket : "))
if age < 12:
    amount = ticket - (ticket*30/100)

elif age > 59 :
    amount = ticket - (ticket * 50/100)
else:
    amount = ticket
    total = total + amount
#p4
age = int(input("Enter the age of p4 : "))
ticket = int(input("Enter the price of ticket : "))
if age < 12:
    amount = ticket - (ticket*30/100)

elif age > 59 :
    amount = ticket - (ticket * 50/100)
else:
    amount = ticket
    total = total + amount
#p5
age = int(input("Enter the age of p5 : "))
ticket = int(input("Enter the price of ticket : "))
if age < 12:
    amount = ticket - (ticket*30/100)

elif age > 59 :
    amount = ticket - (ticket * 50/100)
else:
    amount = ticket
    total = total + amount
print("Total ticket amount =",total)        