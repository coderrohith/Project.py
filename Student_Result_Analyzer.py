marks=[]

n=int(input("Number of subjects:"))

for i in range(n):
    marks.append(int(input("Enter marks :")))

print("Total=",sum(marks))
print("Avarage =",sum(marks)/n)
print("Highest =",max(marks))
print("Lowest=",min(marks))