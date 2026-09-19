#Create a derived class from Student as EnggStudent with :
#a. Data members as :
#i. Branch
#ii. InternalMarks
#b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. override Method CalculateRank
#v. Override __str__ Method
class Student:

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage):
        self.__studentId = studentId
        self.__name = name
        self.__age = age
        self.__percentage = percentage

    # Getters
    def getStudentId(self):
        return self.__studentId

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getPercentage(self):
        return self.__percentage

    # Setters
    def setStudentId(self, studentId):
        self.__studentId = studentId

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

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

    # __str__ Method
    def __str__(self):
        return f"ID: {self.__studentId}, Name: {self.__name}, Age: {self.__age}, Percentage: {self.__percentage}"


# Derived Class
class EnggStudent(Student):

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage, branch, internalMarks):
        super().__init__(studentId, name, age, percentage)
        self.__branch = branch
        self.__internalMarks = internalMarks

    # Getters
    def getBranch(self):
        return self.__branch

    def getInternalMarks(self):
        return self.__internalMarks

    # Setters
    def setBranch(self, branch):
        self.__branch = branch

    def setInternalMarks(self, internalMarks):
        self.__internalMarks = internalMarks

    # Override Accept Method
    def Accept(self):
        super().Accept()
        self.__branch = input("Enter Branch: ")
        self.__internalMarks = float(input("Enter Internal Marks: "))

    # Override Display Method
    def Display(self):
        super().Display()
        print("Branch:", self.__branch)
        print("Internal Marks:", self.__internalMarks)

    # Override CalculateRank Method
    def CalculateRank(self):
        if self.getPercentage() >= 75 and self.__internalMarks >= 75:
            return "Distinction"
        elif self.getPercentage() >= 60:
            return "First Class"
        elif self.getPercentage() >= 50:
            return "Second Class"
        elif self.getPercentage() >= 35:
            return "Pass"
        else:
            return "Fail"

    # Override __str__ Method
    def __str__(self):
        return (f"ID: {self.getStudentId()}, "
                f"Name: {self.getName()}, "
                f"Age: {self.getAge()}, "
                f"Percentage: {self.getPercentage()}, "
                f"Branch: {self.__branch}, "
                f"Internal Marks: {self.__internalMarks}")


# Create EnggStudent object
e1 = EnggStudent(101, "SUJAY", 21, 82.5, "Computer Engineering", 80)

# Display
e1.Display()

# Calculate Rank
print("Rank:", e1.CalculateRank())

# Print object
print(e1)