employees={}

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2.View Employees")
    print("3.Search Employee")
    print("4.Delete Employee")
    print("5.Exit")

    choice=input("Enter your choice:")

    if choice == "1":
        emp_id=input("Employee ID:")
        name=input("Employee Name:")
        salary=input("Salary:")
        employees[emp_id]={"Name":name, "Salary":salary}
        print("Employee Added!")

    elif choice == "2":
        if employees:
            for emp_id, details in employees.items():
                print(f"\nID: {emp_id}")
                print("Name:",details["Name"])
                print("Salary:", details["Salary"])
        else:
            print("No Employees Found!")

    elif choice == "3":
        emp_id = input("Enter Employee ID:")
        if emp_id in employees:
            print(employees[emp_id])
        else:
            print("Employee Not Found!")

    elif choice == "4":
        emp_id=input("Enter employee ID:")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee Deleted!")
        else:
            print("Employee Not Found!")
    elif choice == "5":
        print("Thank You !")
        break

    else:
        print("Invalid Choice")