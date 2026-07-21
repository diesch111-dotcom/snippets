#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_cycle_images_tk2.py

image changes as tk.Button() is clicked
uses itertools.cycle() to cycle through a number of different images
the size of the button and root auto-adjusts to the image size

docs
https://tkdocs.com/tutorial/index.html
https://tkdocs.com/shipman/
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/images.html
https://docs.python.org/3/library/itertools.html
https://docs.python.org/3/library/itertools.html#itertools.cycle

note: newer versions of tkinter allow .gif and .png image files

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import itertools
from functools import partial
import tkinter as tk
import os
   

def toggle(icycle):
    root.title("click on image")
    button1['image'] = next(icycle) 
    

root = tk.Tk()
root.title("Click on the image to cycle")

os.chdir("/home/dietrich/Pictures/image/gif")

# pick a GIF or PNG image you have in the working directory
# or give full path
# 'image' has been made a subdirectory in my main python folder
photo1 = tk.PhotoImage(file='Farm.gif')
photo2 = tk.PhotoImage(file='House.gif')
photo3 = tk.PhotoImage(file='Pond.gif')
photo4 = tk.PhotoImage(file='Sunset.gif')
photo5 = tk.PhotoImage(file='Benz1.gif')
photo6 = tk.PhotoImage(file='LAKE2.gif')
photo7 = tk.PhotoImage(file='art_folk_road2.gif')
photo8 = tk.PhotoImage(file='art_folk_stormcoast2.gif')

# icycle cycles between photo1, photo2, photo3 and photo4 etc.
# you can cycle through more images
icycle = itertools.cycle([photo1, photo2, photo3, photo4, photo5, photo6, 
                          photo7, photo8])
# create a button to display the image
# image will fill the button (adjusts to image size)
button1 = tk.Button(root, image=photo7, command=partial(toggle, icycle))
button1.grid(row=1, column=1)

root.mainloop()
