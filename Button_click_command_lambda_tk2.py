#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_click_command_lambda_tk2.py

Show which tk.Button() has been clicked using lambda 
or partial to pass command arguments

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/tutorial/index.html
https://tkdocs.com/shipman/
https://tkdocs.com/shipman/button.html

curious fact:
in the LinuxMint terminal type:  python3 -m tkinter
to get a small tkinter window showing the version of tkinter you have

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

from functools import partial
import tkinter as tk


def click(name):
    """called with lambda or partial to pass name"""
    s = "button {} has been clicked".format(repr(name))
    root.title(s)
    print(s)


root = tk.Tk()
root.title("click any of the buttons")
# background color of the root window
root['bg'] = 'green'

# only set ULC (x, y) position of root
root.geometry("+{x}+{y}".format(x=250, y=100))

# use lambda (acts as outer closure function) to send an argument to click()
b1 = tk.Button(text="one", width=10, command=lambda: click("one (lambda)"))
# this button uses a partial function for the argument, nice and clean
# width is in letters for strings and pixels for image
b2 = tk.Button(text="two", width=10, command=partial(click, "two (partial)"))

# pack() default is center from top
b1.pack(padx=150, pady=10)
b2.pack(pady=5)

root.mainloop()
