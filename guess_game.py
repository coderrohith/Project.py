import random

number=random.randint(1,10)

guess=int(input("Guess a number between 1 to 10:"))

if guess==number:
    print("Congradulations you guessed correcly.")
else:
    print("wrong guess.")
    print("The correct answer was:",number)