import time

num=int(input("Enter seconds:"))

while num > 0:
    print(num)
    time.sleep(1)
    num -=1

    print("Time's Up!")