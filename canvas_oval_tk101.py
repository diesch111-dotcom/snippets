#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" canvas_oval_tk101.py

The canvas.create_oval() method is used to draw circles and ellipses
coordinates of an imaginary bounding box (rectangle that encloses the oval)
or use a helper function to calulate center and radius of a circle

eg.
canvas.create_oval(x1, y1, x2, y2, fill="yellow", width=4)

fill	The color inside the oval (defaults to empty/transparent).	
    fill="red" or fill="#FF0000"
outline	The color of the border (defaults to black).	outline="blue"
width	The thickness of the border in pixels (defaults to 1).	width=4
dash	Makes the border dashed. Pass a tuple of (dash_length, space_length).	
    dash=(4, 4)
state	Controls visibility. Can be "normal", "hidden", or "disabled".

some info from Google Gemini AI 

Tkinter can use a number of named colors (not case sensitive) like
red, green, blue, white, black, tan, pink, yellow, magenta, lightblue
lightgreen, moccasin, peachpuff, orange, grey, purple, brown
also (light=1 to dark=4) hues of colors like
red1, red2, red3, red4   etc.

tested with LinuxMint and Spyder IDE  dns(vegaseat)  19jun2026
"""

import tkinter as tk

# Set up the main window and canvas
root = tk.Tk()
root.title("tkinter canvas.create_oval() example")
# set the root window's height, width and x,y position
# x,y are the upper left corner ULC coordinates 
# in pixels
w = 450
h = 400
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")


canvas = tk.Canvas(root, width=w, height=h, bg="white")
canvas.pack()

# 1. Draw a CIRCLE (bounding box is a square: 100x100)
# corner coordinates 
ULC = (50, 50)  
LRC = (150, 150)
#canvas.create_oval(50, 50, 150, 150, fill="blue", outline="red", width=2)
canvas.create_oval(ULC, LRC, fill="yellow", outline="red", width=2)

# 2. Draw an OVAL (bounding box is a rectangle: 200x100)
ULC = (180, 50)
LRC = (380, 150)
canvas.create_oval(180, 50, 380, 150, fill="red", outline="blue", width=3)


def create_circle_center(canvas, x, y, r, **kwargs):
    """draws a circle using center (x, y) and radius r"""
    return canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

# draws a circle centered at (200, 250) with a radius of 50
create_circle_center(canvas, 200, 250, 50, fill="white", width=4)


root.mainloop()
