#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' PIL_SierpinskiSquare1.py

create, save (and display( a Sierpinski Carpet/Square fractal pattern
PIL the Python Imaging Library has image processing features
Now called Pillow, a modern, actively maintained fork of PIL
Colors can be given as color name strings

Works seamlessly with Python's tkinter GUI

If your machine does not have Python installed, use this option...
The online C compiler at:
https://www.onlinegdb.com/online_c_compiler#
also runs Python3.  I use it on FireFox to test several computer languages.
(select Python 3 from dropdown menu in upper left corner)
For GUI fans: that Python version comes with tkinter and PIL installed!
Save the picture by clicking the right mouse button on it for a menu.
A little fickle at times on repeats.  This program happens to works okay!

On a Linux terminal use ...
sudo apt-get install python3-pillow
to install pillow if needed

Even though you install pillow, you still use the PIL namespace 
in your Python code.

tested using the Spyder IDE on Linux  dns(vegaseat)  9jul2026
'''

from PIL import Image, ImageDraw


def sierpinski_square(coords, depth, img):
    squares = []
    # check if coordinates form a square
    if coords[1][0] - coords[0][0] == coords[1][1] - coords[0][1]:
        span = coords[1][0] - coords[0][0]
        unit = span/3
        if unit > 1:
            img.rectangle([(coords[0][0]+unit, coords[0][1]+unit),
                (coords[0][0]+2*unit-1,
                coords[0][1]+2*unit-1)],
                fill=(255,255,255), outline=(255,255,255))
        else:
            img.point((coords[0][0]+unit, coords[0][1]+unit),
                fill=(255,255,255))
        for x in range(3):
            for y in range(3):
                # omit the middle square
                if not (x == 1 and y == 1):
                    squares.append([(coords[0][0]+x*unit,
                        coords[0][1]+y*unit),
                        (coords[0][0]+(x+1)*unit,
                        coords[0][1]+(y+1)*unit)])
    else:
        print("coordinates not square")
    if depth > 1:
        for item in squares:
            # the functions calls itself (recursion)
            sierpinski_square(item, depth-1, img)


# set size to a power of 3
# 9**3 works well
size = 9**3
t_size = size
# calculate correct depth
depth = 0
while t_size > 1 and t_size % 3 == 0:
    depth += 1
    t_size = t_size / 3

# testing...
print('depth = {}'.format(depth))  # 6

# drawing will be 'blue' on 'white' (white is default)
canvas = Image.new("RGB", (size, size), color="blue")
image = ImageDraw.Draw(canvas, "RGB")
sierpinski_square([(0,0), (size, size)], depth, image)

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
# look at the saved file with a picture viewer
filename = "PIL_SierpinskiSquare1.png"
canvas.save(filename)
print('image file {} saved'.format(filename))

# nicer...
# show image using Tkinter ...
from PIL import ImageTk
import tkinter as tk

root = tk.Tk()
# only set ULC (x, y) corner position of the root window
root.geometry("+{}+{}".format(150, 100))
root.title(filename)

# convert PIL image objects to Tkinter PhotoImage objects
tk_image1 = ImageTk.PhotoImage(canvas)

# display the image on a label (auto expands to size)
label1 = tk.Label(root,image=tk_image1)
label1.pack(padx=5, pady=5)

root.mainloop()
