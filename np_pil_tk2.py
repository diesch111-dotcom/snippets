#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' np_pil_tk2.py

create an image array and save via PIL

doc
https://scipy.github.io/old-wiki/pages/Numpy_Example_List_With_Doc.html

in the LinuxMint terminal use ...
sudo apt-get install python3-numpy
if needed

tested ++ using the Spyder IDE on Linux  dns aka vegaseat  4jul2026
'''

import numpy as np
from PIL import Image

# create an array of 100x100 ones
ar = np.ones((100, 100), np.float32)

print(ar)  # test

# change to 100X100 array of values 100
ar = ar * 100

print('-'*50)  # 50 dashes, cosmetic
print(ar)      # test

for k in range(0,100):
    ar[k,:] = 100 + (k * 1.5)

print('-'*50)
print(ar)      # test

# use the array to create an image of type "RGB"
img = Image.fromarray(ar,"RGB")

print('-'*50)
print(img)   # test 
print('-'*50)

data = img.getdata()
# show list of the first 10 (r,g,b) tuples
# each rgb value goes from 0 to 255
print(list(data)[:10])
print(len(data))    # 10000  --> 100x100

# save as .png .jpg .gif or .bmp file
# depending on the file extension used
# (the .jpg format gives the smallest file size)
# (the .png format gives the best color quality)
# look at the saved file with a picture viewer
img_file = "np_pil.jpg"
img.save(img_file)

"""
pillow's canvas.show()
brings up the modified image in a viewer, kind of crude, saves the image
as a usually large bitmap file (persists) and calls a .bmp viewer
"""

# nicer...
# show image using Tkinter ...
from PIL import ImageTk
import tkinter as tk

root = tk.Tk()
# only set ULC (x, y) corner position of the root window
root.geometry("+{}+{}".format(150, 100))
root.title(img_file)

# convert PIL image objects to Tkinter PhotoImage objects
tk_image = ImageTk.PhotoImage(img)

# display the image on a label (auto expands to size)
label1 = tk.Label(root, bg='tan', image=tk_image)
label1.pack(ipadx=60, ipady=15)

root.mainloop()
