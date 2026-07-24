#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' mouse_position_relative_tk1.py

Show xy coordinates of mouse click position
relative to root:
event.x, event.y
or relative within a given canvas shape:
event.x - x1, event.y - y1  needs ULC (x1, y1) of widget   

tested with LinuxMint and Spyder IDE   vegaseat  17jul2026
'''

import tkinter as tk
    

def showxy(event):
    '''
    show x, y coordinates of mouse click position
    event.x, event.y relative to ULC of widget 
    '''
    # xy relative to ulc of root window
    #xy = 'root x={}  y={}'.format(event.x, event.y)
    # xy relative to widget needs ULC (x1, y1) of widget
    xy = 'click at x={}  y={}'.format(event.x - x1, event.y - y1)
    root.title(xy)


root = tk.Tk()
root.title("Mouse click within blue rectangle ...")

# create a canvas for drawing
w = 400
h = 400
cv = tk.Canvas(root, width=w, height=h, bg='white')
cv.pack()

# draw a blue rectangle shape with 
# upper left corner coordinates x1, y1
# lower right corner coordinates x2, y2
x1 = 20
y1 = 30
x2 = 380
y2 = 370
cv.create_rectangle(x1, y1, x2, y2, fill="blue", tag='rectangle')

# bind left mouse click within shape rectangle
cv.tag_bind('rectangle', '<Button-1>', showxy)

root.mainloop()
