students=[]

n=int(input("Enter number of students:"))

for i in range(n):
    name=input("Enter student name:")
    status=input("Present or Absent (P/A):")
    students.append([name,status])

print("Attendence Report")

for student in students:
    print(student[0],"-",student[1])