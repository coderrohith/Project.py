products={}

while True:
    print("\n1. Add product")
    print("2.View product")
    print("3. Exit")

    choice=(input("Enter your choice:"))

    if choice=="1":
        name=input(" Product name:")
        qty=int(input(" Quantity:"))
        products[name]=qty

    elif choice == "2":
        for name,qty in products.items():
            print(name,"-",qty)

    elif choice == "3":
        break 