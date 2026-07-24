#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' scale_slider_3slider_color_rgb_tk1.py

tk.Scale() forms 3 sliders, one each for red green blue values

docs
https://tkdocs.com/shipman/scale.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/text.html
https://tkdocs.com/shipman/universal.html

tested with LinuxMint and Spyder IDE   vegaseat  17jul2026
'''

import tkinter as tk


def getnum(event=None):
    """gives a number of value display options"""
    r = scale1.get()  # type --> int
    g = scale2.get()  # type --> int
    b = scale3.get()  # type --> int
    rgb = (r, g, b)
    # Tkinter color format is "#rrggbb"
    hex_color = '#' + "".join("{:02x}".format(k) for k in rgb)
    sf = 'hexstring color = {}'.format(hex_color)
    root.title(sf)
    label1['bg'] = hex_color
    # '1.0' is line1 char 0
    # delete 12 characters in line 1
    text1.delete('1.0', '1.12')
    text1.insert('1.0', hex_color)
    

root = tk.Tk()
# set the root window's height, width and x,y position
# x,y are the upper left corner coordinates in pixels
w = 400
h = 550
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("{}x{}+{}+{}".format(w, h, x, y))
root['bg'] = 'green'
root.title('drag the r, g, b sliders')

# used by scales
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()

# optional for scale3
v3 = tk.IntVar()
# for floats/double use tk.DoubleVar()

# default for orient is vertical
scale1 = tk.Scale(root, orient='vertical', length=400,
    from_=0, to=255, tickinterval=1, command=getnum,
    relief='raised', showvalue=True, variable=v1, label='r')
scale1.set(255)
scale1.grid(row=0, column=1, rowspan=10, padx=5, pady=5)

# default for orient is vertical
scale2 = tk.Scale(root, orient='vertical', length=400,
    from_=0, to=255, tickinterval=1, command=getnum,
    relief='raised', showvalue=True, variable=v2, label='g')
scale2.set(0)
scale2.grid(row=0, column=2, rowspan=10, padx=5, pady=5)

# default for orient is vertical
scale3 = tk.Scale(root, orient='vertical', length=400,
    from_=0, to=255, tickinterval=1, command=getnum,
    relief='raised', showvalue=True, variable=v3, label='b')
scale3.set(0)
scale3.grid(row=0, column=3, rowspan=10, padx=5, pady=5)

myfont = ("arial", 16, "bold")

label1 = tk.Label(root, text="", width=20)
label1.grid(row=11, column=0, columnspan=3, padx=5, pady=5)

# tk.Text() allows copy (ctrl C) of highlighted portion
text1 = tk.Text(root, font=myfont, width=20, height=2, padx=10)
text1.grid(row=12, column=0, columnspan=3, padx=5, pady=5)

# start
getnum()

root.mainloop()
