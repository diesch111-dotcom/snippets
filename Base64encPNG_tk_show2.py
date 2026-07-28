#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Base64encPNG_tk_show2.py

use a base64 encoded image file with Tkinter
use Base64encPNG23.py to generate the encoding

you can use place() and grid()  and
place() and pack() layout managers together,
but not pack() and grid()

tested using the SublimeText IDE on Linux  vegaseat  19jul2026
"""

import pprint
import tkinter as tk

#root = tk.Tk()
root = tk.Tk(className="use a base64 encoded image")  # sets title too
# or give it your title this way
#root.title("My Title")
w = 340
h = 300
x = 50
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("{}x{}+{}+{}".format(w, h, x, y))

rainbow_png_b64='''\
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
'''

photo = tk.PhotoImage(data=rainbow_png_b64)

# optional testing width and height in pixels
print(photo.width())
print(photo.height())

# give it a colorful frame with a relief 
# needs border=8 for the relief to show
frame = tk.Frame(root, bg='green', relief='ridge', border=8)
# frame fills and expands along the the x and y axis
frame.pack(fill='both', expand='yes')

# put the image on a label widget
label1 = tk.Label(frame, image=photo)
label2 = tk.Label(frame, image=photo)
label3 = tk.Label(frame, image=photo)
label4 = tk.Label(frame, image=photo)

# pack() defaults are side='top' and anchor='center'
# or from the center on down
# fill=0, expand=0, ipadx=0, ipady=0, padx=0, pady=0
# ipad is internal padding and pad is external padding
label1.pack()
label2.pack()
label3.pack()
# position a label on the frame using place(x, y)
# place(x=0, y=0) would be the upper left frame corner
label4.place(x=20, y=30)


# extra info
print('dictionary of pack info for label1:')
pack_dict = label1.pack_info()
pprint.pprint(pack_dict)
'''
dictionary of pack info for label1:
{'anchor': 'center',
 'expand': 0,
 'fill': 'none',
 'in': <tkinter.Frame object .!frame>,
 'ipadx': 0,
 'ipady': 0,
 'padx': 0,
 'pady': 0,
 'side': 'top'}
'''

root.mainloop()

#help(base64)
