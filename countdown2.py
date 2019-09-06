# Judd Brau
# Period 7
# countdown.py

from time import sleep
# from art import *

def countdown(x, s):
    if x == 0:
        # tprint("BLAST OFF!!!")
        print("BLAST OFF!!!")
    else:
        # tprint(x)
        print(x, "\b")
        x -= s
        sleep(1)
        countdown(x, s)

step = int(input("What step do you want to count down by? "))
count = int(input("What number do you want to count down from? "))

countdown(count, step)
