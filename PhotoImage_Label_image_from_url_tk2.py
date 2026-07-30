#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" PhotoImage_Label_image_from_url_tk2.py

View an image with Python using the Tkinter GUI toolkit
Get the image from a webpage URL

PIL needed for .jpg images

tested ++ using the SublimeText IDE on Linux  vegaseat  4jul2026
"""

from PIL import ImageTk
import tkinter as tk
import urllib.request as url_lib


root = tk.Tk()
root.title("Tkinter URL Image Viewer")

# URLs with images you can access are getting rare!
# This one is gorgeous!  Hurray to Switzerland!
# get a URL based image from the internet
# if the url is very long, split it in half
part1 = "http://uploads.neatorama.com/wp-content/"
part2 = "uploads/2011/05/cogtrain-500x688.jpg"
url = part1 + part2
picture = url_lib.build_opener().open(url).read()

# use PIL to convert to a format Tkinter can handle
image_tk = ImageTk.PhotoImage(data=picture)

# put the image on a typical widget
# label expands to fit image size
label = tk.Label(root, image=image_tk)
label.pack(padx=5, pady=5)

root.mainloop()
