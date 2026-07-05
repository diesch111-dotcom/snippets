#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" tkinter_layout_pack3.py

a basic look at the tkinter Graphics User Interface GUI...
a button is one of the most fundamental action tkinter GUI widgets
a label/button can show text or image information

creating: label1 = tk.Label(parent, options...)
creating: button1 = tk.Button(parent, options...)
creating: button2 = tk.Button(parent, options...)
etc.

tk.Button() should have some information 'text' and command' action
tk.Label() should have 'text' information

the layout manager pack() is assigned after all the widgets are created
(this gives a better oversight of the layout)
using eg. button1.pack(), button2.pack() ... and label1.pack()
pack() defaults are side='top' and anchor='center'
fill=0, expand=0, ipadx=0, ipady=0, padx=0, pady=0
where ipad is internal padding (eg. text or image) and pad is external padding

docs
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/colors.html

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
# give the root some color, default is a grey white
root.configure(bg="wheat")

# create some widgets
# give the label some background 'bg' color (default is a light grey)
label1 = tk.Label(root, text="information", bg="gold")
# lambda is used to handle the argument arg in label.configure(text=arg)
button1 = tk.Button(root, text="click me!", 
                    command=lambda: label1.configure(text="Hello!"))
button2 = tk.Button(root, text="Heidi",
                    command=lambda: label1.configure(text="Hello Heidi!"))
# add background and foreground color options 
button3 = tk.Button(root, text="Marie", bg="deeppink", fg='white',
                    command=lambda: label1.configure(text="Hello Marie!"))
button_left = tk.Button(root, text="Lefty", bg="lightblue",
                    command=lambda: label1.configure(text="Hello Lefty!"))
button_right = tk.Button(root, text="Righty", bg="lightpink",
                    command=lambda: label1.configure(text="Hello Righty!"))

# now position the widgets, notice the order of packing
# the default for pack() is from the top down and center of root
# padx is used to separate the widgets along the vertical axis
# ipadx pads the text/image within the widget
label1.pack(pady=5, ipadx=10)
button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)
button_left.pack(side="left", padx=10, pady=5)
button_right.pack(side="right", padx=10)

root.mainloop()