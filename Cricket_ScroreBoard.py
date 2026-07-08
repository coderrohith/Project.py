players={}

n=int(input("Enter number of players:"))

for i in range(n):
    name=input("Player Name:")
    runs=int(input("Runs Scored:"))
    players[name]=runs

print("\n Scoredboard")

highest=0
best=""

for name,runs in players.items():
    print(name,"-",runs)

    if runs > highest:
        highest=runs
        best=name

    print("\nHighest Scorer:",best)
    print("Runs:",highest)
