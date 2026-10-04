#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Canvas_create_image_url_tk2.py

Display an image obtained from an internet web page on a tk.Canvas()

features... 
urlopen()
ImageTk.PhotoImage()
canvas.create_image()

VegasEat  03oct2026
'''

import tkinter as tk
from urllib.request import urlopen
# allows jpg
from PIL import ImageTk

root = tk.Tk()
root.title("Display a website image")
# a little more than width and height of largest image
w = 1100
h = 640
x = 80
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("{}x{}+{}+{}".format(w, h, x, y))

# test: loads google logo as a gif image from the webpage
#image_url = "http://www.google.com/intl/en/images/logo.gif"

# split a long url
url1 = "https://arduinomodules.info/wp-content/uploads/"
url2 = "Arduino_KY-037_connection_diagram-1024x650.png"
image_url = url1 + url2

# extract the image name
image_name = image_url.split('/')[-1]
print(image_name)
root.title(image_name)

image_byt = urlopen(image_url).read()
# PIL can create a tk image of a JPEG object too
photo = ImageTk.PhotoImage(data=image_byt)

# create a white canvas
cv = tk.Canvas(bg='white')
# expand into the full root window
cv.pack(side='top', fill='both', expand='yes')

# put the image on the canvas via
# create_image(xpos, ypos, image, anchor)
cv.create_image(10, 10, image=photo, anchor='nw')

root.mainloop()
