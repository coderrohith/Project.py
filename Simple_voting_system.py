a=0
b=0

n=int(input("Number of votes:"))

for i in range(n):
    vote=input("A or B:")

    if vote.upper() == "A":
        a += 1
    elif vote.upper() =="B":
        b += 1

print("Votes for A :",a)
print("Votes for B :",b)

if a>b:
    print("A wins")
elif b<a:
    print("B wins")
else:
    print("Tie")