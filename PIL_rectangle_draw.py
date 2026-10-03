#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' PIL_rectangle_draw.py

Draw a number of rectangles with different color options

featuring...
img = Image.new('RGB', (width, height), color)
draw = ImageDraw.Draw(img)  # the canvas
rect = draw.rectangle([(x,y), (x+w, y+h)], fill=color)
img.save(filename)

rectangle syntax...
rectangle{[ULC, LRC], fill=None, outline=None, width=1) 
you can give it no fill_color but an outline_color and width 

PIL takes some named colors like 'red' or 'yellow'
or color hex strings like '#ff0000' for red
or color rgb_tuple like (255, 0, 0) for red

PIL's show() is a little lame, so use
tkinter to show the image on the computer monitor

in the LinuxMint terminal use...
sudo apt-get install python3-pillow
in the VSCodium terminal use...
python -m pip install pillow
to install pillow if needed
in the code refer to pillow as PIL

tested with Spyder IDE on LinuxMint  VegasEat 19jul2026
'''

from PIL import Image, ImageDraw

# create an empty 'RGB' image
# of size (width, height)
# with a yellow background (default bg color is 'black')
img = Image.new('RGB', (480, 200), 'yellow')

# now create an image surface, a canvas for drawing
draw = ImageDraw.Draw(img)

# this is a method of instance draw
# rectangle{[ULC, LRC], fill=None, outline=None, width=1) 
# ULC = Upper Left Corner (x, y) coordintes
# LRC = Lower Right Corner
# draw a rectangle with just fill
w = 280
h = 180
x = 10
y = 10
rect1 = draw.rectangle([(x,y), (x+w, y+h)], fill='green')

# draw another rectangle with just the outline
w1 = 170
h1 = 180
x1 = 300
y1 = 10
draw.rectangle([(x1,y1), (x1+w1, y1+h1)], fill=None, outline='red', width=4)

# free up resources
del draw

'''
# you can use PIL's img.show()
# this internally saves a bitmap file, then calls the default viewer
# the problem is that these .bmp files are huge and accumulate
# in one of the temp directories on your harddrive
'''

# your choice...
# save as .png, .jpg or.gif file
# depending on the file extension used
# the .jpg format generally gives the smallest file size
# the .png format has no compression loss
# so, save the final image file and then view with an image viewer
filename = "PIL_rectangle_draw.png"
img.save(filename)
print('image file {} written'.format(filename))

# extra...
# show images on the display screen using tkinter
# works on Windows OS, Linux and Apple OSX
import tkinter as tk
from PIL import ImageTk

root = tk.Tk()
root.title(filename)
# only set ULC (x, y) position of root
root.geometry("+{}+{}".format(150, 100))

# convert PIL image object to Tkinter PhotoImage object
tk_image = ImageTk.PhotoImage(img)

# display the image on a label, will expand to fit the image
label = tk.Label(root,image=tk_image)
label.pack(padx=5, pady=5)

root.mainloop()
