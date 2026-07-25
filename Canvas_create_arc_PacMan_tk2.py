#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Canvas_create_arc_PacMan_tk2.py

Explore the Tkinter canvas.create_arc()
Create a Pac-Man triangle optical illusion using three arcs
The arc has a default start at 3 o'cock
extent is in degrees counterclockwise
default style is 'pieslice'

Calculations ...
shaping an equilateral triangle (equal sides and inner angles)
let top corner coordinates be x=150, y=100
let each side be 140 pixels, so side_half = 140/2 = 70
sum of a triangle's inner angles is 180, so each angle is 180/3 = 60
extent = 360 - 60 = 300
height = tan(angle_radians) * side/2 = 121

see also
https://tkdocs.com/shipman/

tested using the Spyder IDE on Linux  vegaseat  19jul2026
'''

import tkinter as tk


def getSquare(x, y, radius):
    """
    given the center coordinates x, y and radius of a circle
    return upper_left x1, y1 and lower_right x2, y2 corner
    coordinates of the bounding square
    """
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    return x1, y1, x2, y2

# root window expands to fit canvas size
root = tk.Tk()
# give it a title
root.title("canvas.create_arc() Pac-Man triangle")

# create a canvas to draw on
cv = tk.Canvas(root, width=300, height=300, bg='white')
cv.pack()

# top
arc1 = cv.create_arc(getSquare(150, 100, 30), start=180+120,
    extent=300, fill='darkgreen', outline='darkgreen')
# left bottom
arc2 = cv.create_arc(getSquare(150-70, 100+121, 30), start=180-120,
    extent=300, fill='red', outline='red')
# right bottom
arc3 = cv.create_arc(getSquare(150+70, 100+121, 30), start=180,
    extent=300, fill='blue', outline='blue')

#line = cv.create_line(50, 130, 250, 180)  # test

root.mainloop()
