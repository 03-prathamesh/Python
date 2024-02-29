import time
timestamp=int(time.strftime('%H:%M:%S'))  # we have to convert it into the integer
print(timestamp)


if(timestamp>=12):
    print("Its afternoon")
elif(timestamp>=5 and timestamp<=9):
    print("Its evening now")
else:
    print("Its night")