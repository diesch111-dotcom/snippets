#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_image_fromfile_toggle_tk2.py

Using itertools.cycle() to create a Tkinter 'ToogleUpDownImageButton'
the up/down images come from files

note: newer versions of tkinter allow .gif and .png image files

docs
https://tkdocs.com/shipman/button.html
https://docs.python.org/3/library/itertools.html

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import itertools as it  # for toggle
import tkinter as tk
import os


class ToogleUpDownImageButton(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('320x100')
        self.title('toggle button up/down images')

        # images are of an up and down button
        # pick GIF or PNG images you have in the working directory or give full path
        self.image_up = tk.PhotoImage(file='btn_up.gif')
        self.image_down = tk.PhotoImage(file='btn_down.gif')

        self.button = tk.Button(self, image=self.image_up, command=self.toggle)
        # pack() default is center from top
        self.button.pack(padx=5, pady=5)
        # cycle through the 2 images
        self.images = it.cycle([self.image_down, self.image_up])
        self.toggle()

    def toggle(self):
        """
        toggle/cycle between up and down button images
        """
        self.button['image'] = next(self.images)


def main():
    app = ToogleUpDownImageButton()
    app.mainloop()

os.chdir("/home/dietrich/Pictures/image/Button")
main()
