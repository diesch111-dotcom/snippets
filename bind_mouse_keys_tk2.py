#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" bind_mouse_keys_tk2.py

Explore the mouse click/motion, wheel events and also key press events

### bind mouse clicks (event.num contains the button number):
'<Button-1>' = left mouse click/press, same as '<ButtonPress-1>' or '<1>'
'<Button-2>' = center on three button mouse
'<Button-3>' = right mouse click 
'<Double-1>' = left mouse doubleclick
'<B1-Motion>' = click left and drag
'<ButtonRelease-1>' = left mouse button released

### bind keys (event.char contains the key's ASCII value):
'<KeyPress>' = any key pressed
'<Return>'   = the enter key has been pressed
'<KeyPress-z>' = z key pressed etc.  also  just '<z>'
'<Up>', '<Down>', '<Left>', '<Right>' catch arrow keys

# Windows
root.bind("<MouseWheel>", mouse_wheel)
# Linux
root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)


tested using the Spyder IDE on Linux  dns(vegaseat)  11jul2026
"""

import tkinter as tk

# a class to the rescue, to give all global variables a safe namespace
class GlobalClass(object):
    """declare all global variables here"""
    x = 0
    #z = False

# now all global variables get a namespace (the class instance)
# use something like ww (from WorldWide) for a recognizable 
# namespace for global variables
ww = GlobalClass()


def info(event):
    info ='You clicked mouse button number', event.num
    root.title(info)
    print(info)  # extra test
    
def change_color(event):
    "change the given widget's color"
    root.config(bg='red')

def show_xy(event):
    '''show x, y coordinates of mouse position
    event.x, event.y relative to ulc of widget
    event.x_root, event.y_root relative to computer screen
    '''
    str = "{} x={} y={}".format('mouse click at', event.x, event.y)
    root.title(str)
    print(str)  # extra test
    
def exit(event):
    "exit the program"
    print('Go, going, gone ...')
    root.destroy() 

def mouse_wheel(event):
    "the mouse pointer has to be over the root area"
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        ww.counter -= 1
    if event.num == 4 or event.delta == 120:
        ww.counter += 1
    str = "root wheel count = {}".format(ww.counter)
    root.title(str)
    print(str)

root = tk.Tk()
root.title("bind() mouse and keys")

# set the root window's width, height and x,y position
# x,y are the upper left corner ULC coordinates 
# in pixels
w = 450
h = 200
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")
# default is a grey white
root.configure(bg="wheat")

button1 = tk.Button(root, text="press me")
# left mouse button click action
button1.bind('<Button-1>', change_color)
# right mouse button click action
button1.bind('<Button-3>', info)
# press the left mouse button to diaplay the mouse coordinates
root.bind('<B1-Motion>', show_xy)
# exit program on left mouse button double click
button1.bind('<Double-1>', exit)
# exit program on Escape key pressed
root.bind('<Escape>', exit)
# the mouae wheel counter is global here
ww.counter = 0
# Windows
root.bind("<MouseWheel>", mouse_wheel)
# Linux
root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)

button1.pack()

root.mainloop()
