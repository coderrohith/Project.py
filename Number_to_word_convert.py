num=int(input("Enter a digit (0/9):"))

words=["Zero","One","Two","Three","Four","Five","six","Seven","Eight","Nine"]

if 0<= num <=9:
    print(words[num])
else:
    print("Enter a single Digit only")