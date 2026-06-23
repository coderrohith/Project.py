import random
import string

length=8
chars=string.ascii_letters + string.digits

password=""

for i in range(length):
    password +=random.choice(chars)

    print(password)