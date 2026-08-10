#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.
n = int(input("Enter the Number of student : "))
total_percentage = 0
for i in range(1,n+1):
    print(f"\nEnter marks of Student {i} : ")
    total_marks = 0
    for j in range(1,6):
        marks = float(input(f"Enter the marks of subject {j} : "))

        total_marks += marks 
    percentage = total_marks / 5
    print(f"percentage of student are {i} = {percentage :.2f}%")

    total_percentage +=percentage
    avarage_percentage = total_percentage / n
    print(f"Avaeage percentage ={avarage_percentage:.2f}%")