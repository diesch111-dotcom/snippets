#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' mouse_position_tk2.py

Show x, y coordinates of mouse click position
event.x, event.y relative to ulc of widget (here root window)
event.x_root, event.y_root relative to root window x_offset, y_offset  
It is y_offset + thickness of title bar in pixels

Bind mouse clicks and show coordinates of click
'<Button-1>' = left mouse click (same as '<ButtonPress-1>' or '<1>')

tested with LinuxMint and Spyder IDE   vegaseat  17jul2026
'''

import tkinter as tk
    

def show_xy(event):
    '''
    show x, y coordinates of mouse click position
    event.x, event.y relative to ulc of widget (here root window)
    event.x_root, event.y_root relative to display window
    '''
    # ULC click shows point (51, 132)  root y + title bar thickness
    xy = "x={}  y={}".format(event.x_root, event.y_root)
    # point (0, 0) will be ULC of root window
    #xy = "x={}  y={}".format(event.x, event.y)
    root.title(xy)


# create the main window
root = tk.Tk()
root.title("click on the window area")
w = 400
h = 300
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("{}x{}+{}+{}".format(w, h, x, y))

# bind left mouse click inside the main window
root.bind('<Button-1>', show_xy)

# execute event loop
root.mainloop()
