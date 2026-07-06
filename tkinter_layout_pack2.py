#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" tkinter_layout_pack2.py

a basic look at the tkinter Graphics User Interface GUI...
a button is one of the most fundamental action tkinter GUI widgets
a label shows text or image information

creating: button1 = tk.Button(parent, options...)
creating: label1 = tk.Label(parent, options...)

when a widget is created it is given a unique identifier one
then assigns it a variable with a slightly more recognizable name
Python has some rules on variable naming, above all use KISS
I like the underline separator, a habit from the C days

tk.Button() should have some information 'text' and command' action
tk.Label() should have 'text' information

the layout manager pack() is assigned after all the widgets are created
using eg. button1.pack() and label1.pack()
pack() defaults are side='top' and anchor='center'
fill=0, expand=0, ipadx=0, ipady=0, padx=0, pady=0
where ipad is internal padding and pad is external padding


using the Spyder IDE on Linux  dns(vegaseat) 4jul2026
"""

import tkinter as tk


# need a window to place widgets into
root = tk.Tk()
# set the root window's width, height and x,y position
# x,y are the upper left corner ULC coordinates 
# in pixels
w = 450
h = 200
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")

# create some widgets
# give label some color (default is a light grey)
label1 = tk.Label(root, text="information", bg="gold")
# lambda is used to handle the argument arg in label.configure(text=arg)
button_click = tk.Button(root, text="click me!", 
                    command=lambda: label1.configure(text="Hello!"))
# testing only
button_test = tk.Button(root)

# just for curiousity look at the given identifier
# sometimes these come up in error messages
print(button_click)  # .!button
print(button_test)   # .!button2
print(label1)        # .!label

# now position the widgets, notice the order of packing
# pady is used to separate the widgets along the vertical y axis
label1.pack(pady=5)
button_click.pack(pady=5)
button_test.pack()

root.mainloop()
