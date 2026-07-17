#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Canvas_create_text_marquee_ticker_tk2.py

Using a tk.Ccanvas() to create a marquee/ticker via
canvas.create_text(x, y, anchor='nw', text=s, font=font)
canvas.move(object, x_increment, y_increment)

docs
https://tkdocs.com/shipman/canvas.html
https://tkdocs.com/shipman/create_text.html
https://tkdocs.com/shipman/canvas-methods.html


tested using the Spyder IDE on Linux  dns aka vegaseat  16jul2026
'''

import tkinter as tk


root = tk.Tk()
root.title('Chicken road politics')

canvas = tk.Canvas(root, height=80, width=600, bg="yellow")
canvas.pack()

font = ('courier', 48, 'bold')

text_width = 15
s1 = "We don't really care why the chicken crossed the road.  "
s2 = "We just want to know if the chicken is on our side of the "
s3 = "road or not. The chicken is either for us or against us.  "
s4 = "There is no middle ground here.  (George W. Bush)"
s5 = "    In other news ....  "
s6 = "Harvey Dummkopf the inventor of the caps lock key passed away!"
# pad front and end of text with spaces
s7 = ' ' * text_width
# concatenate it all
st = s7 + s1 + s2 + s3 + s4 + s5 + s6 + s7

x = 1
y = 20
text = canvas.create_text(x, y, anchor='nw', text=st, font=font)

dx = 1
dy = 0  # use horizontal movement only
while True:
    # move text object by increments dx, dy
    # -dx --> right to left movement
    canvas.move(text, -dx, dy)
    canvas.update()
    # shorter delay time --> faster movement
    # millisecond integer value
    canvas.after(5)

root.mainloop()
