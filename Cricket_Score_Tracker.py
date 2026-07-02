runs=[]

n=int(input("Number of balls:"))

for i in range(n):
    run=int(input("Runs Scored:"))
    runs.append(run)

print("Total Runs:",sum(runs))
print("Height Run Ball:",max(runs))