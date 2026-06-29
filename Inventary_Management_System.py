items={}

while True:
    print("\n1.Add Items")
    print("2.View items")
    print("3.Update Quantity")
    print("4.Exit")

    choice=input("Choice:")

    if choice == "1":
        name=input("Item Name:")
        qty = int(input("Quantity:"))
        items[name]=qty

    elif choice =="2":
        for name, qty in items.items():
            print(name,":",qty)

    elif choice == "3":
        name=input("Item name:")
        if name in items:
            items[name] = int(input("New Quantity:"))
            print("Updated!")
        else:
            print("Item Not Found!")

    elif choice == "4":
        break