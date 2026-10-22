#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" image_splash_label_tk2.py

create a noframe splash screen
destroy the splash screen after a set time

vegaseat  22oct2026
"""

import tkinter as tk
# to allow .jpg files
from PIL import ImageTk

root = tk.Tk()
# no frame
root.overrideredirect(True)  

img_file = "splash.jpg"
image = ImageTk.PhotoImage(file=img_file)
# use a label as an image panel, adjusts to image size
panel = tk.Label(root, image=image)
panel.pack(side='top', fill='both', expand='yes')

panel.update()
# wait 8000 milliseconds or whatever
panel.after(8000)
root.destroy()

root.mainloop()
