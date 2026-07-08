#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Button_toggle_tk2.py

Create a tk.Button() and use a class Static to toggle colors

The Spyder IDE 'New File...' command gives the 2 leading Shebangs/Hashbangs
lines that tell a Unix based system about Python3 location and which codex 
to use, it also adds a triple quote comment area ---  nice!

tested using the Spyder IDE on Linux  dns(vegaseat)  4jul2026
"""

import tkinter as tk


class Static:
    '''call Static.toggle()'''
    state = False
    @classmethod
    def toggle(self):
        '''toggles between True and False'''
        self.state = not self.state
        return self.state


def root_color():
    '''
    toggle the background 'bg' color between two colors
    using an external class Static
    '''
    # toggles between True and False
    if Static.toggle():
        root.config(bg='red')
    else:
        root.config(bg='gold')


root = tk.Tk()
root.title("click on 'Toggle Color' button")
# set the root window's width, height and x,y position
# x,y are the upper left corner ULC coordinates 
# measured in pixels
w = 450
h = 200
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry(f"{w}x{h}+{x}+{y}")
# initial color
root.config(bg='gold')

# create a button, command runs the given function ref
# when button is clicked
button1 = tk.Button(
    root, 
    text="Toggle Color", 
    command=root_color)

button1.pack()

root.mainloop()
