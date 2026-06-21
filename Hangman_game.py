word="python"
guessed=""

turns=6

while turns >0:
    failed=0

    for ch in word:
        if ch in guessed:
            print(ch,end="")
        else:
            print("_",end="")
            failed += 1

    print()

    if failed == 0:
        print("You won!")
        break

    guess=input("Guess a letter:")
    guessed += guess

    if guess not in word :
        turns -= 1
        print("Wrong Guess")
        print("Turns Left",turns)

if turns == 0:
    print("You Lost!")