total_days = int(input("Enter the number of day : "))
year =  total_days // 365
remaining_days = total_days % 365

week = remaining_days // 7
days = remaining_days // 7

print("year =", year)
print("week =",week)