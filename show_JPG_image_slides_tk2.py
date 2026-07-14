#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" show_JPG_image_slides_tk2.py

Display a number of images as a simple slide show using Tkinter.
For .jpg files apply PIL ImageTk so tkinter can show them.

docs
http://tkinter.unpythonic.net/wiki/PhotoImage
https://tkdocs.com/shipman/
https://tkdocs.com/shipman/images.html

Use a PIL ImageTk object to display a photo image on a button.
Have the popcorn ready! Click on the image to stop the show!  

tested using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
"""

import tkinter as tk
from PIL import ImageTk
import os
# Could change the folder to the one the pictures are in.
#os.chdir('path/to/picture_dir')

# testing ,,,
# just in case your image files are simply in there for testing
print(os.getcwd())

# create the root window
root = tk.Tk()
# set ULC (x, y) position of root window
root.geometry("+{}+{}".format(70, 100))
 
# create a list of image file names you have
# could be digital pictures you took or appropriately seized
# (you can add more files as needed)
# pick image files you have in your working directory or use a full path
# PIL ImageTk converts ,jpg fies so tkinter can use them.
# Why .jpg files?  They are usually much smaller in byte size.
# since Stuttgart was my home town, let look at "Benzes"
image_files = [
"Benz1.jpg",
"Benz2.jpg",
"Benz3.jpg",
"Benz4.jpg",
"Benz5.jpg"
]

# use a button to display the slides
# this way a simple mouse click on the button stops the show
# the button 'automagically' expands to fit the photo image
button = tk.Button(root, command=root.destroy)
button.pack(padx=5, pady=5)

# delay in seconds (time each slide shows) you select
# use .after() and not time.sleep() or you freeze tk
delay = 10

print("="*30)

# delayed for loop
for image_file in image_files:
    # beginning update
    root.update()
    print(image_file)
    if os.path.exists(image_file) == False:
        print("{} does not exiat!".format(image_file))
        root.destroy()
    # PIL will create a tk image object from a JPEG file
    img_tk = ImageTk.PhotoImage(file=image_file)
    root.title(image_file)
    button["image"] = img_tk
    # update again
    root.update()
    # finally the delay, takes a milliseconds integer value
    root.after(int(delay*1000))

# execute the event loop
root.mainloop()
