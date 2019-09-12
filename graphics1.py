# Judd Brau
# Period 7
# graphics1.py

from graphics import *
from time import sleep
import math

def genHex(center, r):
    if type(center) != tup:
        raise error("center parameter must be type tup not type {}".format(type(center)))
    points = [Point(center[0], center[1]-r)]
    a = (2*sqrt(3))/d
    b = 2/d
    c = 
    points.append(Point(center[0]-((2*sqrt(3))/d), center[1]-(2/d)))

    return Polygon(points)


def main():
    win = GraphWin("Window 1", 500, 500)

    hex = genHex(15, 5)
    hex.draw(win)

    win.getMouse()
    win.close()



if __name__ == '__main__':
    main()
