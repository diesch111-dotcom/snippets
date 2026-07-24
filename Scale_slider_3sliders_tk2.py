#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Scale_slider_3sliders_tk2.py

Experimenting with Tkinter's Scale (slider) widget

potential application:
for mortgage payments use this and a couple of sliders/spinboxes-->
# monthly interest rate given % annual interest
interest_rate = interest/(100 * 12)
# total number of payments
payment_num = years * 12
# calculate monthly payment
payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))

or a rgb color chooser using 3 sliders for each r, g, b color

share 2 sliders, one showing Celcius the other Fahrenheit values

for details see ...
http://www.python-course.eu/tkinter_sliders.php
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/scale.html
https://tkdocs.com/shipman/scale.html

tested with LinuxMint and Spyder IDE   vegaseat  17jul2026
'''

import tkinter as tk


def getnum(event):
    """gives a number of value display options"""
    x = scale1.get()  # type --> int
    s = "scale1 = {}".format(x)
    label1.configure(text=s)
    label3['text'] = "scale3 = %s" % scale3.get()  # type --> float
    root.title("scale1 and scale2 v = %s" % v.get())

root = tk.Tk()
# only set size of root
w = 390
h = 220
root.geometry("{}x{}".format(w, h))
root['bg'] = 'green'
root.title('tk.Scale()')

# shared by 2 scales, ties sliders together
v = tk.IntVar()
# optional for scale3
v3 = tk.IntVar()
# for floats/double use tk.DoubleVar()

# optionally pick a font you have
myfont = ("arial", 16, "bold")
label1 = tk.Label(root, text="", fg="blue", font=myfont)
label1.grid(row=0, column=0)

label3 = tk.Label(root, text="", fg="red", font=myfont)
label3.grid(row=1, column=0)

# showvalue=False (default is True) will not show
# scale value next to slider
scale1 = tk.Scale(root, orient='horizontal', length=200,
    from_=0, to=100, tickinterval=25, command=getnum,
    label='drag slider', showvalue=False, variable=v)
scale1.set(0)
scale1.grid(row=2, column=0, padx=5)

# sharing variable=v ties these scales together
# default for orient is vertical
scale2 = tk.Scale(root, orient='vertical', length=200,
    from_=0, to=100, tickinterval=2.5, command=getnum,
    relief='raised', showvalue=True, variable=v)
scale2.set(0)
scale2.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

# exploring a few more options
# scale is set in float values scale3.get() will be a float
scale3 = tk.Scale(root, orient='vertical', length=200,
    from_=0.0, to=100.0, tickinterval=10, command=getnum,
    resolution=0.5,
    relief='raised', showvalue=True, #variable=v3,
    width=10, fg='red', trough="yellow")
scale3.set(50)
scale3.grid(row=0, column=2, rowspan=3, padx=5, pady=5)

root.mainloop()
