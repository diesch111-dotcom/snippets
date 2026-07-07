#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Vacation_Spinbox1.py

Let's say you are the head of a family and the pressure is on to go on 
a vacation to the "LaLaLand" fun resort.  To figure out the cost of this
you want to show off and use a python tkinter GUI program.  

What is a really useful widgets here?
tk.Spinbox()  uses arrow symbols to change values up or down

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/spinbox.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/grid.html


using the Spyder IDE on Linux  dns(vegaseat) 8jul2026
"""

import tkinter as tk


def spinbox_changed():
    '''
    value.get() or spinbox.get() are strings
    convert to integer value with int()
    '''
    cost = int(spinbox1.get())
    days = int(spinbox2.get())
    total_cost = cost * days * PPD_cost
    label3.configure(text=f"total cost is ${total_cost:,.2f}")
    # for testing...
    print(f"spin_box1 value = {value1.get()} person")
    print(f"spin_box2 value = {value2.get()} day")
    print(f"total cost is ${total_cost:,.2f}/day")



root = tk.Tk()
root.title("Our Vacation to LaLaLand")
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

# estimated Person Per Day cost
# entry ticket, food, lodging
PPD_cost = 180

# another way to handle values created by widgets
# value=1 is initial value
value1 = tk.StringVar(value=1)
value2 = tk.StringVar(value=1)

# tk.Spinbox() from 0 to 12 in steps of 1 (default)
# Python already has keyword 'from' so 'from_' is used
# size adjusts to applied font
spinbox1 = tk.Spinbox(
    root,
    from_=0,
    to=12,
    increment=1,
    font=('courier', 20, 'bold'),
    textvariable=value1,  # via tk.StringVar()
    wrap=True,
    foreground='red',
    width=3,   # characters
    command=spinbox_changed)

label1 = tk.Label(
    root, 
    text="Number of people:", 
    font=('courier', 20, 'bold'))

spinbox2 = tk.Spinbox(
    root,
    from_=0,
    to=12,
    increment=1,
    font=('courier', 20, 'bold'),
    textvariable=value2,  # via tk.StringVar()
    wrap=True,
    foreground='red',
    width=3,   # characters
    command=spinbox_changed)

label2 = tk.Label(
    root, 
    text="Number of days:", 
    font=('courier', 20, 'bold'))

label3 = tk.Label(
    root, 
    text="result", 
    font=('courier', 20, 'bold'))

# show initial result
spinbox_changed()

# here the grid layout manager works best
# sticky='w' means west (left side)
label1.grid(row=0, column=0, pady=5, padx=10, sticky='w')
label2.grid(row=1, column=0, pady=5, padx=10, sticky='w')
# columnspan=2 keeps the text expanding in column=0 from pushing column=1
label3.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky='w')
spinbox1.grid(row=0, column=1, sticky='w')
spinbox2.grid(row=1, column=1, sticky='w')

root.mainloop()
