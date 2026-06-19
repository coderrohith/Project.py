score=0

print("=====PYTHON QUIZ=====")

ans=input("1.What is the capital of india?:")

if ans.lower()=="new Delhi":
    score += 1

ans=input("2.How many days are their in a week?:")

if ans=="7":
    score += 1

ans=input("3.What is 5+5?:")

if ans=="10":
     score += 1

print("\n Your score+",score,"/3")