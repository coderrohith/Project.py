items=[]

n=int(input("Hiow many items?:"))

for i in range(n):
    price=float(input("Enter Item Price:"))
    items.append(price)

    print("Total Bill=",sum(items))