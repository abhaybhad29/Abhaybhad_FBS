#Create a class MedicalStudent inherited from Student with following
#i. Data members :Specialization
#ii. MarksOfInternship
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

    # CalculateRank Method
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
        return (f"ID: {self.__studentId}, "
                f"Name: {self.__name}, "
                f"Age: {self.__age}, "
                f"Percentage: {self.__percentage}")


# MedicalStudent Derived Class
class MedicalStudent(Student):

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage,
                 specialization, marksOfInternship):

        # Calling Parent Constructor
        super().__init__(studentId, name, age, percentage)

        self.__specialization = specialization
        self.__marksOfInternship = marksOfInternship

    # Getters
    def getSpecialization(self):
        return self.__specialization

    def getMarksOfInternship(self):
        return self.__marksOfInternship

    # Setters
    def setSpecialization(self, specialization):
        self.__specialization = specialization

    def setMarksOfInternship(self, marksOfInternship):
        self.__marksOfInternship = marksOfInternship

    # Override Accept Method
    def Accept(self):
        super().Accept()

        self.__specialization = input("Enter Specialization: ")
        self.__marksOfInternship = float(
            input("Enter Marks of Internship: ")
        )

    # Override Display Method
    def Display(self):
        super().Display()

        print("Specialization:", self.__specialization)
        print("Marks of Internship:", self.__marksOfInternship)

    # Override CalculateRank Method
    def CalculateRank(self):

        if self.getPercentage() >= 75 and self.__marksOfInternship >= 75:
            return "Distinction"

        elif self.getPercentage() >= 60 and self.__marksOfInternship >= 60:
            return "First Class"

        elif self.getPercentage() >= 50:
            return "Second Class"

        elif self.getPercentage() >= 35:
            return "Pass"

        else:
            return "Fail"

    # Override __str__ Method
    def __str__(self):
        return (
            f"ID: {self.getStudentId()}, "
            f"Name: {self.getName()}, "
            f"Age: {self.getAge()}, "
            f"Percentage: {self.getPercentage()}, "
            f"Specialization: {self.__specialization}, "
            f"Internship Marks: {self.__marksOfInternship}"
        )


# Creating MedicalStudent Object
m1 = MedicalStudent(
    201,
    "Sakshi",
    21,
    82.5,
    "Cardiology",
    85
)

# Display
m1.Display()

# Calculate Rank
print("Rank:", m1.CalculateRank())

# __str__
print(m1)