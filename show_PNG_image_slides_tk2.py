#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" show_PNG_image_slides_tk2.py

Display a number of images as a simple slide show using Tkinter.

Newer versions of tkinter (8.6+) handle .gif and .png image files
ImageTk from PIL is still needed for .jpg image files.

docs
http://tkinter.unpythonic.net/wiki/PhotoImage
https://tkdocs.com/shipman/
https://tkdocs.com/shipman/images.html

Use a tk.PhotoImage object to display a photo image on a button.
Have the popcorn ready! Click on the image to stop the show!  


tested using the Spyder IDE on Linux OS  dns aka vegaseat  13jul2026
"""

import tkinter as tk
import os
# Could change the folder to the one the pictures are in.
#os.chdir('path/to/picture_dir')

# testing ,,,
# just in case your image files are simply parked in there
print(os.getcwd())

# create the root window
root = tk.Tk()
# set ULC (x, y) position of root window
root.geometry("+{}+{}".format(70, 100))
 
# create a list of image file names you have
# could be digital pictures you took or appropriated (licitly seized)
# (you can add more files as needed)
# pick image files you have in your working directory or use a full path
# tk.PhotoImage() allows .gif   .png   .bmp formats
# since Stuttgart was my home town, let us watch "Benzes"
image_files = [
"Benz1.png",
"Benz2.png",
"Benz3.png",
"Benz4.png",
"Benz5.png"
]

# use a button to display the slides
# this way a simple mouse click on the button stops the show
# the button automagically expands to fit the photo image
button = tk.Button(root, command=root.destroy)
button.pack(padx=5, pady=5)

# delay in seconds (time each slide shows)  you select value
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
    # create a tk image object
    img_tk = tk.PhotoImage(file=image_file)
    root.title(image_file)
    button["image"] = img_tk
    # update again
    root.update()
    # finally the delay, takes a milliseconds integer value
    root.after(int(delay*1000))

# execute the event loop
root.mainloop()
