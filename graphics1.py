# Judd Brau
# Period 7
# graphics1.py

from graphics import *
from time import sleep
import math

def genHex(center, r):
    if type(center) != tuple:
        raise Exception("center parameter must be type tup not type {}".format(type(center)))
    a = (r*math.sqrt(3))/2
    b = r/2
    return Polygon(
        Point(center[0], center[1]-r),
        Point(center[0]-a, center[1]-b),
        Point(center[0]-a, center[1]+b),
        Point(center[0], center[1]+r),
        Point(center[0]+a, center[1]+b),
        Point(center[0]+a, center[1]-b)
    )

def smile(size, ex, win):
    a,b = 250,250;
    eyeCol = color_rgb(75, 135, 196)

    cir = Circle(Point(a, b), size)
    cir.setFill(color_rgb(224, 157, 81))
    cir.draw(win)

    p1 = Point(a-(size/3), b-(size/3))
    p2 = Point(a+(size/3), b-(size/3))
    eye1 = Circle(p1, 15)
    eye2 = Circle(p2, 15)

    eye1.setOutline(eyeCol)
    eye2.setOutline(eyeCol)
    eye1.setFill(eyeCol)
    eye2.setFill(eyeCol)

    eye1.draw(win)
    eye2.draw(win)

    if ex:
        smile = 0

def main():
    win = GraphWin("Window 1", 500, 500)

    # hex = genHex((250, 250), 50)
    # hex.draw(win)
    # hex1 = genHex((100, 100), 100)
    # hex1.draw(win)

    face = smile(100, 0, win)
    # face.draw(win)

    win.getMouse()
    win.close()



if __name__ == '__main__':
    main()
