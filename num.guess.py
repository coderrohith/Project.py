import random

number=random.randint(1,20)

for i in range(5):
    guess=int(input("Guess a number:"))

    if guess == number:
        print("You win!")
        break
    elif guess<number:
        print("Too Low")
    else:
        print("Too High")
else:
    print("The number was",number)
      
