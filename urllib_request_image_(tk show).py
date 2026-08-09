#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' urllib_request_image_(tk show).py

Retrieve and save an image from a web page
Show image with tkinter
please see:
Debian -- The Universal Operating System.html

IDLE usually comes with Python install, to gain access...
might have to install the IDLE IDE, in the Linux terminal use:
sudo apt update
sudo apt install idle3
...once installed this way, it shows up under 'Programming' as IDLE

tested with IDLE IDE on LinuxMint  vegaseat 19jul2026
'''

import urllib.request
#import urllib.request as url_open

# find yourself a picture on an internet web page you like
# (right click on the picture, look under properties and copy the address)
#picture_page = "http://www.google.com/intl/en/images/logo.gif"
picture_page = "http://www.smartlinks.org/revenge2.gif"

# open the web page picture and read it into a variable
my_opener = urllib.request.build_opener()
my_page = my_opener.open(picture_page)
my_picture = my_page.read()

# get image file name via slicing
filename = picture_page[-10:]

print("Image saved as:", filename)
'''
Image saved as: venge2.gif
'''

# save the image file
with open(filename, "wb") as fout:
    fout.write(my_picture)

# show image using Tkinter ...
# PIL ImageTk also allows formats other than gif or png
from PIL import ImageTk
import tkinter as tk

root = tk.Tk()
# only set ULC (x, y) corner position of the root window
root.geometry("+{}+{}".format(150, 100))
root.title(filename)

#  to Tkinter PhotoImage object
tk_image1 = ImageTk.PhotoImage(file=filename)

# display the image on a label (auto expands to size)
label1 = tk.Label(root,image=tk_image1)
label1.pack(padx=5, pady=5)

root.mainloop()
