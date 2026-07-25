#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' center_root_window_tk2.py

Center the Tkinter window on the display screen

tested using the Spyder IDE on Linux  vegaseat  19jul2026
'''

import tkinter as tk


def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y adjustments for title bar = 20
    x = (ws//2) - (w//2)
    # deduct titlebar
    y = (hs//2) - (h//2) - 20
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


root = tk.Tk()
root.title('centered screen position')
root['bg'] = 'lime'
root.update_idletasks()

center_window(500, 300)

root.mainloop()
