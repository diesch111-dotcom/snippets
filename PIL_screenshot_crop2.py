#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" PIL_screenshot_crop2.py

this webside offers free images 
https://stock.adobe.com/discover/nature
but the image links don't work!!!!'
at least bring up the picture on the screen and press the
'prt sc' button and then crop the saved screen picture 
using the PIL crop feature

it's under /Pictures/  eg.
/home/admin123/PicturesScreenshot from 2026-07-10 01-31-20.png
this one is AI generated...
/home/admin123/PicturesScreenshot from 2026-07-10 02-44-55.png

bring up the screen file with the 'GNU Image Manipulation Program' 
it shows the mouse cursor location at the bottom 
jot it dow, enter it in the crop() funtion, correct it as the 
cropped picture shows

program 'image_label_mouse_tk2.py' creates a file 'coordinates.txt'
cut and paste from there (extra trailing comma is tolerated) 

could rename the file and ao on ...

tested with LinuxMint and Spyder IDE   vegaseat  17jul2026
"""

from PIL import Image #, ImageFont, ImageDraw, ImageOps
import os

# Linux:
os.chdir("/home/admin123/Pictures")
# pick an image you have in the working /Picture folder
image_file =\
"Screenshot from 2026-07-22 10-02-23.png"
pict_screen = Image.open(image_file)


# region to be cropped out of the picture
# you can get the corner coordinates with the GNU Image Manipulation Program
# program 'image_label_mouse_tk2.py' creates a file 'coordinates.txt'
# cut and paste from there (extra trailing comma is tolerated) 
# box shape  ULC and LRC coordinates (left, upper, right, lower)
cropped = pict_screen.crop((706, 174, 1214, 961, ))

"""
pillow's canvas.show()
brings up the modified image in a viewer, kind of crude, saves the image
as a usually large bitmap file (persists) and calls a .bmp viewer
"""

# better...
# save as .png .jpg .gif or .bmp file
# depending on the file extension used
# (the .jpg format gives the smallest file size)
# (the .png format gives the best color quality)
# actually these .png files are denser then .jpg
# look at the saved file with a picture viewer
filename = 'Screenshot_cropped.png'
cropped.save(filename)
print('file {} saved in {}'.format(filename, "/home/dietrich41/Pictures/"))
#print(f"{cropped.size = }")
width, height = cropped.size
total_pixels = width * height
print("{} x {} = {:,} pixels".format(width, height, total_pixels))

# nicer...
# show image using Tkinter ...
from PIL import ImageTk
import tkinter as tk

root = tk.Tk()
# only set ULC (x, y) corner position of the root window
root.geometry("+{}+{}".format(150, 100))
root.title("/home/admin123/Pictures" + filename)

# convert PIL image objects to Tkinter PhotoImage objects
tk_image1 = ImageTk.PhotoImage(cropped)

# display the image on a label (auto expands to size)
label1 = tk.Label(root,image=tk_image1)
label1.pack(padx=5, pady=5)

root.mainloop()
