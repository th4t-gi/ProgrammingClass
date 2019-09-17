# Judd Brau
# Period 7
# graphics2.py

from graphics import *
from random import randint
from time import sleep

snowArray = []

def genSnowflake(x, option):
    if not(randint(0,3)):
        o = randint(0, 4)
        s = randint(1, 10)
        x = randint(0, width)

        sf = genSnowflake(x, o)
        sf.draw(win)
        snowArray.append([sf, x, s])

        return Image(Point(x,-50), "snowflakes/snowflake{}.png".format(option))

def draw(window):


def main():
    width, height = 500, 500
    win = GraphWin("Window 1", width, height)
    win.setBackground(color_rgb(80, 80, 80))

    for i in range(200):
        time.sleep(.3)
        for j in snowArray:
            flake, x, s = j[0], j[1], j[2]
            p1 = flake.getAnchor().getY()
            flake.move(0, s*3)

    win.getMouse()
    win.close()

try:
    main()
except GraphicsError:
    print("window closed")
