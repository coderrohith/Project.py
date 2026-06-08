m1=float(input("Enter marks in subject1:"))
m2=float(input("Enter marks in subject2:"))
m3=float(input("Enter marks in subject3:"))

total=m1+m2+m3
average=total/3

print("Total marks=",total)
print("Average=",average)

if average>=90:
    print("Grade A")
elif average>=75:
    print("Grade B")
elif average>=50:
    print("Grade C")
else:
    print("Grade D")