#Create a class College which has collection of students. Add the
#following methods :
#a. Parameteried constructor for number of students.
#b. AddStudent
#c. GetStudent
#d. RemoveStudent
#e. Override __str__ Method
class College:

    # Parameterized Constructor
    def __init__(self, numberOfStudents):
        self.__numberOfStudents = numberOfStudents
        self.__students = []

    # Add Student
    def AddStudent(self, student):
        if len(self.__students) < self.__numberOfStudents:
            self.__students.append(student)
            print("Student added successfully.")
        else:
            print("College is full. Cannot add more students.")

    # Get Student
    def GetStudent(self, studentId):
        for student in self.__students:
            if student.getStudentId() == studentId:
                return student

        print("Student not found.")
        return None

    # Remove Student
    def RemoveStudent(self, studentId):
        for student in self.__students:
            if student.getStudentId() == studentId:
                self.__students.remove(student)
                print("Student removed successfully.")
                return

        print("Student not found.")

    # Override __str__
    def __str__(self):
        result = "College Students:\n"

        for student in self.__students:
            result += str(student) + "\n"

        return result