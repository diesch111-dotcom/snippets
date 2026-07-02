#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" canvas_text_tk101.py

The canvas.create_text() method in Tkinter is used to place text inside your 
canvas.

eg.
canvas.create_text(x, y, text="Your Text Here", **options)

x, y: The anchor coordinate where the text will be positioned.
text: The actual string you want to display. Use \n for multiline text.
options: Optional arguments to customize the font, color, alignment, and 
    positioning anchor.

font	A tuple containing (font_family, size, "modifiers"). 
    Modifiers like "bold", "italic", or "underline" are optional.	
    font=("Helvetica", 12, "bold italic")
fill	The color of the text (defaults to black).
anchor  Controls which part of the text string is attached to the
    (x, y) coordinate. 
    Options: tk.N, tk.NE, tk.E, tk.SE, tk.S, tk.SW, tk.W, tk.NW, or 
    tk.CENTER (default).
    anchor=tk.NW (top-left)
justify	 How multi-line text wraps internally. 
    Options: tk.LEFT, tk.CENTER, or tk.RIGHT.
angle	Rotates the text counter-clockwise by a given number of degrees.
width	Forces the text to automatically wrap onto a new line once it reaches 
    this width in pixels.

some info from Google Gemini AI 

Tkinter can use a number of named colors (not case sensitive) like
red, green, blue, white, black, tan, pink, yellow, magenta, lightblue
lightgreen, moccasin, peachpuff, orange, grey, purple, brown
also (light=1 to dark=4) hues of colors like
red1, red2, red3, red4   etc.

tuple examples of common fonts (some might be available just on Windoze)
(family, size, weight)
times48b = ('times', 48, 'bold')
times20b = ('times', 20, 'bold')
times12n = ('times', 12, 'normal')
cour20b = ('courier', 20, 'bold')
helv20bi = ('helvetica', 20, 'bold italic')
verd20bi = ('verdana', 20, 'bold italic')
cosa24b = ('Comic Sans MS', 24, 'bold')
helv16b = ('helvetica', 16, 'bold')
# 'normal' is default
arial25n = ['Arial', 25]
calibri12bu = ('calibri', 12, 'bold', 'underline')

tested with LinuxMint and Spyder IDE  dns(vegaseat)  19jun2026
"""

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Text Example")
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

# 1. Simple text (Centered exactly at X=200, Y=50)
canvas.create_text(200, 50, text="Hello, Tkinter Canvas!", 
                   font=("Arial", 16, "bold"), fill="darkblue")

txt_ml="This is multi-line text\nthat is centered horizontally\ninside its own block.",
# 2. Multi-line text with center alignment
canvas.create_text(200, 130, text=txt_ml, font=("Courier", 12), 
                   justify=tk.CENTER, fill="green")

# 3. Left-aligned text using the 'anchor' option
# (The point 50, 230 acts as the top-left corner of the text box instead of the center)
canvas.create_text(50, 230, text="• Bullet Point A\n• Bullet Point B", 
                   font=("Times", 14), anchor=tk.NW, fill="red")

# Create the text and save its ID
score_text = canvas.create_text(50, 300, text="Score: 0", anchor=tk.NW)

# Later in your code, update it like this:
canvas.itemconfig(score_text, text="Score: 100")

root.mainloop()