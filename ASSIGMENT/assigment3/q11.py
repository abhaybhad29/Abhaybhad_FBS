total = 0

# Person 1
age = int(input("Enter age of Person 1: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    amount = ticket - (ticket * 30 / 100)
elif age > 59:
    amount = ticket - (ticket * 50 / 100)
else:
    amount = ticket

total = total + amount

# Person 2
age = int(input("Enter age of Person 2: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    amount = ticket - (ticket * 30 / 100)
elif age > 59:
    amount = ticket - (ticket * 50 / 100)
else:
    amount = ticket

total = total + amount

# Person 3
age = int(input("Enter age of Person 3: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    amount = ticket - (ticket * 30 / 100)
elif age > 59:
    amount = ticket - (ticket * 50 / 100)
else:
    amount = ticket

total = total + amount

# Person 4
age = int(input("Enter age of Person 4: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    amount = ticket - (ticket * 30 / 100)
elif age > 59:
    amount = ticket - (ticket * 50 / 100)
else:
    amount = ticket

total = total + amount

# Person 5
age = int(input("Enter age of Person 5: "))
ticket = float(input("Enter ticket amount: "))

if age < 12:
    amount = ticket - (ticket * 30 / 100)
elif age > 59:
    amount = ticket - (ticket * 50 / 100)
else:
    amount = ticket

total = total + amount

print("Total Ticket Amount =", total)