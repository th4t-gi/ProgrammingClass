# Judd Brau
# Period 7
# countdown.py

from time import sleep
# from art import *

step = int(input("What step do you want to count down by? "))
count = int(input("What number do you want to count down from? "))

while count > 0:
    # tprint(count)
    print(count)
    count -= step
    sleep(1)

# tprint("BLAST OFF!!!")
print("BLAST OFF!!!")
