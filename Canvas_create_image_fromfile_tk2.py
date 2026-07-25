#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Canvas_image_create_fromfile_tk2.py

Display an image file using Tkinter and PIL
PIL allows Tkinter to read more than just .gif and .png image files

note: newer versions of tkinter allow .gif and .png image files
ImageTk from PIL is still needed for .jpg image files

use widget.update() and widget.after(milliseconds) followed by another 
widget.update() for a delay action that works well with tkinter

https://tkdocs.com/shipman/create_image.html

tested using the Spyder IDE on Linux  vegaseat  4jul2026
'''

from PIL import ImageTk
# Python3
import tkinter as tk

root = tk.Tk()
w = 600
h = 620
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("{}x{}+{}+{}".format(w, h, x, y))

# pick an image file you have in your working directory
# or specify full path
image_file = "../image/LAKE2.png"
#image_file = "../image/chemist3.gif"
#image_file = "../image/PurpleHouse.gif"
#image_file = "../image/Heidrun.BMP"
root.title(image_file)

# convert to an image object tkinter can handle
# option needed for JPG files, works for GIF and PNG too
photo = ImageTk.PhotoImage(file=image_file) 
# native option for GIF and PNG files 
#photo = tk.PhotoImage(file=image_file)  
print(photo)        # test eg. pyimage1
print(image_file)
print(image_file.split('/')[-1])

# put the image on a canvas
cv = tk.Canvas()
cv.pack(side='top', fill='both', expand='yes')
# upper left corner of image is on canvas(x,y)
img = cv.create_image(0, 0, image=photo, anchor='nw')
cv.update()

# optionally delete image after 8000 ms
#cv.after(8000, cv.delete(img))
#cv.update()

root.mainloop()
