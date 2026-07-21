#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_toggle-(class-static)_tk2.py

Make a toggle button with Tkinter using a Static class toggle

docs
https://tkdocs.com/shipman/entry.html
https://tkdocs.com/shipman/button.html

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import tkinter as tk

class Static:
    '''can be called with Static.toggle()'''
    k = False
    @classmethod
    def toggle(self):
        '''toggles between True and False'''
        self.k = not self.k
        return self.k

def entryColor():
    '''
    toggle the entry color between white and red
    using an external class
    '''
    # toggles between True and False
    if Static.toggle():
        edit1.config(bg='red')
    else:
        edit1.config(bg='white')


root = tk.Tk()
root.title("click on 'Toggle Color' button")

# only set ULC (x, y) position of root
root.geometry("+{x}+{y}".format(x=250, y=150))

# create a button, command runs the given function ref
# when button is clicked
btn1 = tk.Button(root, text="Toggle Color", command=entryColor)
btn1.pack(fill=tk.BOTH, expand=1)

# us a font to make entry() widget taller
times48b = ('times', 48, 'bold')
# create an entry box to color
edit1 = tk.Entry(root, font=times48b, bg='tan', width=10)
edit1.pack(fill=tk.BOTH, expand=1)

root.mainloop()
