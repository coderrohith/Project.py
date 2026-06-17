expenses=[]

n=int(input("How many expenses?:"))

for i in range(n):
    amount=float(input("Enter expense:"))
    expenses.append(amount)

    print("Total Expense =",sum(expenses))
    print("Avarage Expense =",sum(expenses)/n)
