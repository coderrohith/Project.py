text=input("Enter text:")
shift=int(input("Enter shift value:"))

result=""

for ch in text:
    if ch.isalpha():
        new=chr(ord(ch)+ shift)
        result +=new
    else:
        result += ch

print("Encrypted Text :",result)