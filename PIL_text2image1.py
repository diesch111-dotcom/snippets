''' PIL_text2image1.py
Add rotated text to an image using PIL
The text is drawn in its own blank image and rotated
then superimposed on the background image.

fnt = ImageFont.truetype("../image/Fonts/comic.ttf", 28)

PIL the Python Imaging Library has image processing features
Now called Pillow, a modern, actively maintained fork of PIL
Colors can be given as color name strings or color tuples.

Works seamlessly with Python's tkinter GUI

On a Linux terminal use ...
sudo apt-get install python3-pillow
to install pillow if needed

Even though you install pillow, you still use the PIL namespace 
in your Python code.

tested using the Spyder IDE on Linux  dns(vegaseat)  9jul2026
'''

from PIL import Image, ImageFont, ImageDraw, ImageOps

# pick an image you have in the working folder
# or give full file path
image_file = "../image/girl102.jpg"
img = Image.open(image_file)

# try...
# create a font object with comic font size 28
fnt = ImageFont.truetype("../image/Fonts/comic.ttf", 28)

txt_img = Image.new('L', (180, 80))
txt_drw = ImageDraw.Draw(txt_img)
# fill=255 is yellow
txt_drw.text((0, 0), "Pretty Flower", font=fnt, fill='white')
w = txt_img.rotate(45, expand=1)

img.paste(ImageOps.colorize(w, 'black', 'yellow'), (5, 5),  w)

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
# actually these .png files are denser then .jpg
# look at the saved file with a picture viewer
filename = 'PIL_image_add_text_tk1.png'
img.save(filename)
print('file {} saved'.format(filename))

# nicer...
# show image using Tkinter ...
from PIL import ImageTk
import tkinter as tk

root = tk.Tk()
# only set ULC (x, y) corner position of the root window
root.geometry("+{}+{}".format(150, 100))
root.title(filename)

# convert PIL image objects to Tkinter PhotoImage objects
tk_image1 = ImageTk.PhotoImage(img)

# display the image on a label (auto expands to size)
label1 = tk.Label(root,image=tk_image1)
label1.pack(padx=5, pady=5)

root.mainloop()
