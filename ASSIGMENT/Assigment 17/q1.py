#1. Create a class Student with following
#a. data members :
#i. StudentId
#ii. Name
#iii. Age
#iv. Percentage
#b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. Method CalculateRank
#v. Override __str__ Method

class Student:

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage):
        self.__studentId = studentId
        self.__name = name
        self.__age = age
        self.__percentage = percentage

    # Getter and Setter for StudentId
    def getStudentId(self):
        return self.__studentId

    def setStudentId(self, studentId):
        self.__studentId = studentId

    # Getter and Setter for Name
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # Getter and Setter for Age
    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    # Getter and Setter for Percentage
    def getPercentage(self):
        return self.__percentage

    def setPercentage(self, percentage):
        self.__percentage = percentage

    # Accept Method
    def Accept(self):
        self.__studentId = int(input("Enter Student ID: "))
        self.__name = input("Enter Name: ")
        self.__age = int(input("Enter Age: "))
        self.__percentage = float(input("Enter Percentage: "))

    # Display Method
    def Display(self):
        print("Student ID:", self.__studentId)
        print("Name:", self.__name)
        print("Age:", self.__age)
        print("Percentage:", self.__percentage)

    # Calculate Rank
    def CalculateRank(self):
        if self.__percentage >= 75:
            return "Distinction"
        elif self.__percentage >= 60:
            return "First Class"
        elif self.__percentage >= 50:
            return "Second Class"
        elif self.__percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    # Override __str__ Method
    def __str__(self):
        return (f"ID: {self.__studentId}, "
                f"Name: {self.__name}, "
                f"Age: {self.__age}, "
                f"Percentage: {self.__percentage}")


# Creating object
s1 = Student(101, "Abhay", 21, 82.5)

# Display
s1.Display()

# Getter
print("Student Name:", s1.getName())
print("Percentage:", s1.getPercentage())

# Setter
s1.setName("Rahul")
s1.setPercentage(68.5)

print("\nAfter Updating:")
s1.Display()

# Calculate Rank
print("Rank:", s1.CalculateRank())

# __str__
print(s1)