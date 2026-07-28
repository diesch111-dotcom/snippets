#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button-(multiple-via-loop)_tk2.py

Create multiple Tkinter buttons using list comprehension

https://tkdocs.com/shipman/button.html

tested with LinuxMint and SublimeText IDE   vegaseat  17jul2026
'''

from functools import partial
import tkinter as tk


class ManyButtons(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("10 buttons")
        myfont = ('Comic Sans MS', 14, 'bold')
        # create button 1 to 9 using a list comprehension
        self.buttons = [tk.Button(
            self.root, 
            width=20,
            text='{}'.format(k+1),
            command=partial(self.do_command, k+1)
            ) 
        for k in range(9)]
        # lay out the buttons
        for btn in self.buttons:
            btn.pack(pady=2)
            btn.config(relief='raised', bd=10, font=myfont)
        # bind the buttons to an action
        for n, btn in enumerate(self.buttons):
            btn.bind('<Button-1>', partial(self.do_binding, n))

    def do_command(self, k):
        print('command {}'.format(k))

    def do_binding(self, k, event):
        print('binding {} {}'.format(k+1, event.widget))

    def run(self):
        self.root.mainloop()


# test the module
if __name__ == '__main__':
    ManyButtons().run()
