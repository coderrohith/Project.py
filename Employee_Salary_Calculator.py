name=input("Enployee Name:")
basic=float(input("Enter basic salary:"))

hra=basic*0.20
da=basic*0.15
gross=basic+hra+da

print("\n Salary Slip")
print("Employee:",name)
print("Basic Salary:",basic)
print("HRA:",hra)
print("DA::",da)
print("Gross Salary:",gross)
