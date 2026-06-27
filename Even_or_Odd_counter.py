numbers=[]

n=int(input("How many numbers ? :"))

for i in range(n):
    numbers.append(int(input("Enter Number:")))

even=0
odd=0

for num in numbers:
    if num %2 ==0:
        even +=1
    else:
        odd +=1

print("Even Numbers:",even)
print("Odd Numbers:",odd)

