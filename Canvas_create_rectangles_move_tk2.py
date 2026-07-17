#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Canvas_create_rectangles_move_tk2.py

Tkinter animate via canvas.move(obj, xAmount, yAmount)
objects are two rectangles

canvas.move(obj, xAmount, yAmount)
# milliseconds integer value
canvas.after(50)
canvas.update()

doc
https://tkdocs.com/shipman/canvas.html
https://tkdocs.com/shipman/create_rectangle.html


tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import tkinter as tk

# create the basic window, let's call it 'root'
root = tk.Tk()
root.title("Move canvas rectangles")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# canvas.create_rectangle(x0, y0, x1, y1, option, ... )
# x0, y0, x1, y1 are corner coordinates of ulc to lrc diagonal
rc1 = canvas.create_rectangle(20, 260, 120, 360, outline='white', fill='blue')
rc2 = canvas.create_rectangle(20, 10, 120, 110, outline='white', fill='red')

# increments for move
y = x = 5
for k in range(50):
    # milliseconds integer value
    canvas.after(50)
    # move rectangle by increments x, y 
    # interesting code
    canvas.move(rc1, x, -y)
    canvas.move(rc2, x, y)
    canvas.update()

root.mainloop()
