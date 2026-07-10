feet = float(input("Enter the feet : "))
inches = float(input("Enter the inches : "))

total_inches = (feet*12) + inches
total_cm = total_inches * 2.54
meter = total_cm / 100

print("Distance into meter =",meter)
print("Distance into cm =",total_cm)