#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' canvas_create_oval_multi_tk2.py

Using Tkinter canvas.create_oval(rect, fill=None, outline='black', width=1)
and two for loops draw a series of circles to form a 3D 'artsy' look,
given are the radius and center coordinates of the circles.

If rect is a square then draw a circle (otherwise it's an oval)
If fill is given a color then the circle is filled with this color.
Width is the width of the outline, width=0 avoids any outline/border

Helper fnctions are:   
def draw_circle(x, y, radius, color)
def get_square(x, y, radius)

FYI:  I jam my 'caps lock' key with a toothpick

tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import tkinter as tk


def draw_circle(x, y, radius, color=None, width=None):
    '''
    draw a circle with given radius, center coordinates x,y and color
    default outline color is black
    '''
    #print('color={}  width={}'.format(color, width))  # test
    # to draw a circle you need to get the upper left
    # and lower right corner coordinates of a square
    rect = get_square(x, y, radius)
    # draw the cicle that fits into the rect/square
    # outline is a color and width is the width of the outline
    cv.create_oval(rect, fill=color, outline='black', width=width)

def get_square(x, y, radius):
    '''
    given the center=(x, y) and radius
    calculate the square for a circle to fit into
    return x1, y1, x2, y2 of the square's ulc=(x1, y1) and
    lrc=(x2, y2) diagonal corner coordinates
    '''
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    return x1, y1, x2, y2


# create the basic window, let's call it 'root'
root = tk.Tk()
# only set x=100, y=80 position of root window upper left corner
# root will expand to fit canvas size
root.geometry("+%d+%d" % (100, 80))
root.title("canvas.create_oval() to make a series of circles")

# create a canvas to draw on
cv = tk.Canvas(root, width=600, height=600, bg='green')
# position the canvas via a pack() layout
cv.pack()

color = 'red'
radius = 20
limit = 15
for k in range(1, limit):
    x = 25 * k
    y = 25 * k
    radius = radius + 2 * k
    draw_circle(x, y, radius, color=color, width=3)
 
# this loop counts down
for k in range(limit-1, 1, -1):
    x = 25 * k + int(150 * 1/k)
    y = 25 * k
    radius = radius - 2 * k
    draw_circle(x, y, radius, color=color, width=3)

root.mainloop()
