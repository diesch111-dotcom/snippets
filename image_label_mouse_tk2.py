#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" image_label_mouse_tk2.py

Use a tk.Label() to display an image and show the coordinates the mouse
cursor is pointing at relative to the image.
Upper Left Corner ULC and Lower Right Corner LRC coordinates are needed 
for the PIL crop((x1 ,y1, x2, y2)) function

program 'image_label_mouse_tk2.py' creates a file 'coordinates.txt'
cut and paste from there (extra trailing comma is tolerated) 

tested using the Spyder IDE on Linux  dns aka vegaseat  4jul2026
"""

#from PIL import Image
import tkinter as tk
import os
    

def show_xy(event):
    '''
    show x, y coordinates of mouse click position
    event.x, event.y relative to ulc of widget (here root window)
    event.x_root, event.y_root would be relative to display window
    '''
    xy = "x={}  y={}".format(event.x, event.y)
    xy2 = "{}, {}, ".format(event.x, event.y)  # cut/paste format
    root.title(xy)
    print(xy)
    print(xy2)
    fname = "coordinates.txt"
    # "a" will append to an existing file
    with open(fname, "a") as fout:
        fout.write(xy2)

root = tk.Tk()
root.title('image as label background')

# Linux places 'prt sc' key action here
os.chdir("/home/admin123/Pictures")
# pick a .gif or .png image file you have 
image_file =\
"Screenshot from 2026-07-22 10-02-23.png"
pict = tk.PhotoImage(file=image_file)

# get the width and height of the image
w = pict.width()
h = pict.height()
print("width = {}  height = {}".format(w, h))
print("Corner coordinates for crop(): ")
# position coordinates of root 'upper left corner'
x = 200
y = 50
# size the root to fit the image
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

fname = "coordinates.txt"
if os.path.exists(fname) == True:
    os.remove(fname)

# bind left mouse click inside the main window
root.bind('<Button-1>', show_xy)

label = tk.Label(root, image=pict)
label.pack()

# execute event loop
root.mainloop()

