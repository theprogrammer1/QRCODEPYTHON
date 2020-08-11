import time
seconds = int(input("How many seconds for the timer: "))
for i in range(seconds):
    print(str(seconds - i) + "seconds remain")
    time.sleep(1)
