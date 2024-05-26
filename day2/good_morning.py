import time

timeStr = time.strftime("%H:%M", time.localtime())

if timeStr < "12:00":
    print("Good morning!")
elif timeStr < "17:00":
    print("Good afternoon!")
else:
    print("Good evening!")  