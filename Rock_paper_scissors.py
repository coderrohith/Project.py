import random

items=["rock,paper,scissors"]

computer=random.choice(items)

print("DEBUG computer value:",computer)

user=input("Enter rock,paper or scissors:").strip().lower()

print("Computer chose:",computer)

if user == computer:
    print("Draw")
elif(user=="rock" and computer=="scissors")or\
    (user=="paper" and computer=="rock")or\
    (user=="scissors" and computer=="paper"):
    print("You win!")
else:
    print("You lose")