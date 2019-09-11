# Judd Brau
# Period 7
# turtle.py
import time
from turtle import *

def square(x):
    for i in range(4):
        forward(x)
        right(90)

def spiral(a, theta, b=1, t=0):
    if t >= 20:
        return
    circle(a, 90)
    left(theta)
    spiral(a+b, theta, a, t=t+1)

spiral(1, 0)
time.sleep(10)
