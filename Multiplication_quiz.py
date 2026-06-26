import random 

a=random.randint(1,10)
b=random.randint(1,10)

answer=int(input(f"What is {a}*{b}?:"))

if answer == a*b:
    print("Correct!")
else:
    print("Wrong1 Answer is ",a*b)