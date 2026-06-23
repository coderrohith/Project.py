balence=1000

amount = int(input("Enter amount to withdraw:"))

if amount <= balence:
    balence -= amount
    print("Remaining Balence:",balence)
else:
    print("Insufficient Balence")