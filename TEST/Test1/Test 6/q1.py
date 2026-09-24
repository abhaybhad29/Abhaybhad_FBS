#Write a program which calculates toll calculation on some location following
#is data provided:
#Many vehicles goes through the toll every vehicle has to pay the basic
#toll + extra charges if any.
#two wheelers have to pay basic toll Rs 20 three wheelers have to pay
#30 and four wheelers have to pay 40
#heavy veheicles i.e. Vehicles having wheels more than four, have to
#pay 60 Rs as basic toll
#extra charges :
#for two wheelers if no. of persons are more than two extra charge
#=10/person
#for three wheelers if no. of persons are more than 3 extra charge
#=20/person
#for four wheelers if no. of persons are more than 4 extra charge
#=40/person
#for heavy vehicle if no. of person are more than 6 extra charges
#=100/person.
#Show polymorphic behaviour in main. Main module should be
#designed in such way that toll should easily operate it through
#interactive menu driven program .
#Object of vehicle class should not be possible.
from abc import ABC, abstractmethod


# Abstract Parent Class
class Vehicle(ABC):

    def __init__(self, wheels, persons):
        self.wheels = wheels
        self.persons = persons

    @abstractmethod
    def calculate_toll(self):
        pass

    def display(self):
        print("Number of Wheels:", self.wheels)
        print("Number of Persons:", self.persons)


# Two Wheeler
class TwoWheeler(Vehicle):

    def __init__(self, persons):
        super().__init__(2, persons)

    def calculate_toll(self):
        toll = 20

        if self.persons > 2:
            extra_persons = self.persons - 2
            toll = toll + (extra_persons * 10)

        return toll


# Three Wheeler
class ThreeWheeler(Vehicle):

    def __init__(self, persons):
        super().__init__(3, persons)

    def calculate_toll(self):
        toll = 30

        if self.persons > 3:
            extra_persons = self.persons - 3
            toll = toll + (extra_persons * 20)

        return toll


# Four Wheeler
class FourWheeler(Vehicle):

    def __init__(self, persons):
        super().__init__(4, persons)

    def calculate_toll(self):
        toll = 40

        if self.persons > 4:
            extra_persons = self.persons - 4
            toll = toll + (extra_persons * 40)

        return toll


# Heavy Vehicle
class HeavyVehicle(Vehicle):

    def __init__(self, wheels, persons):
        super().__init__(wheels, persons)

    def calculate_toll(self):
        toll = 60

        if self.persons > 6:
            extra_persons = self.persons - 6
            toll = toll + (extra_persons * 100)

        return toll


# Main Function
def main():

    while True:

        print("\n========== TOLL MANAGEMENT SYSTEM ==========")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            persons = int(input("Enter number of persons: "))

            vehicle = TwoWheeler(persons)

            print("\n--- Toll Details ---")
            vehicle.display()
            print("Basic Toll: Rs. 20")
            print("Total Toll: Rs.", vehicle.calculate_toll())


        elif choice == 2:

            persons = int(input("Enter number of persons: "))

            vehicle = ThreeWheeler(persons)

            print("\n--- Toll Details ---")
            vehicle.display()
            print("Basic Toll: Rs. 30")
            print("Total Toll: Rs.", vehicle.calculate_toll())


        elif choice == 3:

            persons = int(input("Enter number of persons: "))

            vehicle = FourWheeler(persons)

            print("\n--- Toll Details ---")
            vehicle.display()
            print("Basic Toll: Rs. 40")
            print("Total Toll: Rs.", vehicle.calculate_toll())


        elif choice == 4:

            wheels = int(input("Enter number of wheels: "))

            if wheels <= 4:
                print("Heavy vehicle must have more than 4 wheels.")
                continue

            persons = int(input("Enter number of persons: "))

            vehicle = HeavyVehicle(wheels, persons)

            print("\n--- Toll Details ---")
            vehicle.display()
            print("Basic Toll: Rs. 60")
            print("Total Toll: Rs.", vehicle.calculate_toll())


        elif choice == 5:

            print("Thank you for using Toll Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Calling main
main()