#Write a program to check if entered year is a leap year or not.
def leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


year = int(input("Enter year: "))

if leap_year(year):
    print("Leap year")
else:
    print("Not a leap year")