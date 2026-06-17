text=input("Enter a sentence:")

words=text.split()

for word in set(words):
    print(word,":",words.count(word))