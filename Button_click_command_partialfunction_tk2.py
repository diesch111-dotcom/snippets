#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_click_command_partialfunction_tk2.py

Show which tk.Button() has been clicked using command and partial function
Here partial function passes command arguments. nice clean setup

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/tutorial/index.html
https://tkdocs.com/shipman/
https://tkdocs.com/shipman/button.html
https://tkdocs.com/tutorial/index.html

curious fact:
in the LinuxMint terminal type:  python3 -m tkinter
to get a small tkinter window showing the version of tkinter you have

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

from functools import partial
import tkinter as tk


def click(name):
    """called with a partial function to pass name"""
    s = "{} clicked via partial()".format(repr(name))
    root.title(s)
    print(s)


root = tk.Tk()
root.title("click any of the buttons")
# background color of the root window
root['bg'] = 'tan'

# only set ULC (x, y) position of root
root.geometry("+{x}+{y}".format(x=250, y=200))

# partial takes care of function and argument
btn1 = tk.Button(text="one", command=partial(click, "one"))
btn2 = tk.Button(text="two", command=partial(click, "two"))
btn3 = tk.Button(text="three", command=partial(click, "three"))

# pack() default is center from top first
# root window will expand to fit the pack() layout
btn1.pack(padx=150, pady=10)
btn2.pack(pady=5)
btn3.pack(pady=5)

root.mainloop()
