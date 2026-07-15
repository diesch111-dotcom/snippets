''' PIL_DrawLinesOnImage_tk2.py

Opens an image and draws diagonal lines over it.
Show the resulting image with tkinter.

Colors can be color name strings for PIL or tkinter.

On a Linux terminal use ...
sudo apt-get install python3-pillow
to install pillow if needed

works with LinuxMint and Spyder IDE  dns aka vegaseat  15jun2026
'''

from PIL import Image, ImageDraw

# load a picture file tou have
# if that does not work give the full file path 
image_file = "../image/flowers.jpg"
img = Image.open(image_file)
# (width, height)
print(img.size)    # (359, 300)
# width
print(img.size[0]) # 359
# "L" (luminance) for greyscale images,
# "RGB" for true colour images, and "CMYK" for pre-press images
print(img.mode)  # RGB

draw = ImageDraw.Draw(img)

print((0, 0) + img.size) # (0, 0, 359, 300)
# draw diagonal lines
# draw.line((x1, y1, x2, y2), width=0, fill=None)
# from ULC = UpperLeftCorner x1,y1 to LRC = LowerRightCorner x2,y2
draw.line((0, 0) + img.size, fill='gold')
#from LLC = LowerLeftCorner x1,y1 to URC = UpperRightCorner x2,y2
draw.line((0, img.size[1], img.size[0], 0), fill='gold')

# free up resources
del draw

"""
pillow's canvas.show()
brings up the modified image in a viewer, kind of crude, saves the image
as a usually large bitmap file (persists) and calls a .bmp viewer
"""

# or better save the image as .gif or .png  or .jpg
# (the .jpg format usually gives the smallest file size)
# look at the saved image file in an editor or image viewer
filename = 'PIL_DrawLinesOnImage.jpg'
# or specify in save() eg. img.save(filename, "PNG")
img.save(filename)
print('file {} written'.format(filename))

# or show image using Tkinter ...
from PIL import ImageTk
import tkinter as tk

root = tk.Tk()
# only set ULC (x, y) position of root (optional)
root.geometry("+{}+{}".format(150, 100))
root.title(filename)

# convert PIL image objects to Tkinter PhotoImage objects
tk_image1 = ImageTk.PhotoImage(img)

# display the images on labels
label1 = tk.Label(root,image=tk_image1)
label1.pack(padx=5, pady=5)

root.mainloop()
