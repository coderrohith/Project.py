cart=[]

while True:
    item=input("Enter item name:")
    price=float(input("Enter item price:"))

    cart.append((item,price))

    ch=input("Add more items (yes/no):")

    if ch.lower() !="yes":
        break

    print("\nShopping Cart")
    total=0

    for item in cart:
        print(item,"-",price)
        total +=price

    print("Total Bill=",total)