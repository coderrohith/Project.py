tasks=[]

while True:
    task=input("Enter task (or exit):")

    if task == "exit":
        break

    tasks.append(task)

print("Your Tasks:")

for i in tasks:
    print("-",i)