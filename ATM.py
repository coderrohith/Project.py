balence=5000

print("Welcome to ATM")
print("1 Check Balence")
print("2 Deposit")
print("3 Withdraw")

choice=int(input("Enter your choice:"))

if choice==1:
    print("Balence=",balence)

elif choice==2:
    amount=float(input("Enter deposit amount:"))
    balence +=amount
    print("New Balence=",balence)

elif choice==3:
    amount=float(input("enter withdrawal amount:"))
    if amount<=balence:
        balence -=amount
        print("New balence=",balence)
    else:
        print("Insufficient Balence")

else:
    print("Invalid choice")

              

