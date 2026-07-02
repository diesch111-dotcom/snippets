#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" canvas_rectangle_tk101.py

The canvas.create_rectangle() method in Tkinter is used to draw rectangles 
and squares

eg.
canvas.create_rectangle(x1, y1, x2, y2, **options)

x1, y1: coordinates of the upper-left corner ULC
x2, y2: coordinates of the lower-right corner LRC
options: Optional arguments to customize colors, borders, and interaction.

fill	The color inside the rectangle (defaults to transparent/empty).	
    fill="gold"
outline	The color of the border (defaults to black). 
    Use outline="" to hide it.	outline="black"
width	The thickness of the border in pixels (defaults to 1).	width=3
dash	Makes the border dashed. Pass a tuple of (dash_length, space_length).	
    dash=(5, 5)
activedash / activefill	Changes the border style or fill color when the mouse 
    hovers over it.

some info from Google Gemini AI 

can form a rectangle with a line and larger width

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
root.title("tkinter canvas.create_rectangle() example")
# set the root window's height, width and x,y position
# x,y are the upper left corner ULC coordinates 
# in pixels
w = 450
h = 480
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")


canvas = tk.Canvas(root, width=w, height=h, bg="white")
canvas.pack()

# 1. A solid colored rectangle
# Top-left at (50, 50), Bottom-right at (200, 120)
canvas.create_rectangle(50, 50, 200, 120, fill="salmon", outline="darkred")

# 2. A perfect square (Width and height are both 80 pixels)
# Top-left at (250, 50), Bottom-right at (330, 130)
canvas.create_rectangle(250, 50, 330, 130, fill="lightblue", outline="blue", 
                        width=2)

# 3. A hollow rectangle with a thick, dashed border
# Top-left at (50, 180), Bottom-right at (350, 250)
canvas.create_rectangle(50, 180, 350, 250, outline="purple", width=4, 
                        dash=(6, 4))

# a thick blue from point(50,50) to point(400, 50) forms a rectangle
canvas.create_line(50, 350, 400, 350, fill="blue", width=59)

root.mainloop()