text=input("Enter text:")

for ch in set(text):
    print(ch,":",text.count(ch))