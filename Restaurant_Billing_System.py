menu={
    "Pizza":150,
    "Burger":100,
    "Sandwich":80,
    "Coffee":50,
    "Tea":20,
}
 
total=0

while True:
    print("\n-----MENU-----")
    for item,price in menu.items():
        print(item,"-",price)

    item=input("\n Enter item name:")

    if item in menu:
        qty=int(input("Enter item quantity:"))
        bill=menu[item]*qty
        total=bill
        print("Item Total=",bill)
    else:
        print("Iten Not Available!")

    choice=input("Enter your choice:")

    if choice.lower()!="yes":
        break

print("\n-----BILL-----")
print("Total Amount=",total)
print("Thaank You! Visit Again.")

