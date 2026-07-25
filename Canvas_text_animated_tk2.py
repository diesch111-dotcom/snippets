#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Canvas_text_animated_tk2.py

Display text on a Tkinter canvas and move/bounce the text around

tk_Canvas()
canvas.create_text(x, y, text, fill, font)
canvas.move()
canvas.after(msec)
canvas.update()
canvas.bbox()

docs
https://tkdocs.com/shipman/canvas.html

tested using the Spyder IDE on Linux  vegaseat  19jul2026
"""
'''

import random
import tkinter as tk
    
# seed the random generator with a time value (default)
random.seed()

root = tk.Tk()
# root window adjusts to the size of the canvas
root.title("Canvas bouncing 'Hello World' text")


wide = 400
high = 400
canvas = tk.Canvas(root, width=wide, height=high, bg='blue')
canvas.pack()

# canvas.create_text(x, y, text, fill, font)
text = canvas.create_text(100, 300, text="Hello World",
    fill='Yellow', font=('Helvetica', 30, 'bold'))

x1 = random.randint(1,6)
y1 = random.randint(1,6)

while True:
    canvas.move(text, x1, y1)
    # update after 30 milli-seconds
    canvas.after(30)
    canvas.update()
    # returns a rectangle enclosing the given object on the canvas
    # the top left corner of the rectangle is (bx1, by1)
    # the bottom right corner is (bx2, by2)
    bx1, by1, bx2, by2 = canvas.bbox(text)
    if bx1 < 0 or bx2 > wide or by1 < 0 or by2 > high:
        x1 = random.randint(1,6)
        y1 = random.randint(1,6)
    # make it bounce of the wall/edge
    # left edge
    if bx1 < 0:
        x1 = abs(x1)
    # right edge
    elif bx2 > wide:
        x1 = -abs(x1)
    # top edge
    if by1 < 0:
        y1 = abs(y1)
    # bottom edge
    elif by2 > high:
        y1 = -abs(y1)
  

root.mainloop()
