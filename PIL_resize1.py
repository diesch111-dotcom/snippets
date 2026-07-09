''' PIL_resize1.py

This code snipper uses PIL (pillow) to resize an image.
PIL the Python Imaging Library has image processing features
Now called Pillow, a modern, actively maintained fork of PIL

Works seamlessly with Python's tkinter GUI

On a Linux terminal use ...
sudo apt-get install python3-pillow
to install pillow if needed

Even though you install pillow, you still use the PIL namespace 
in your Python code.

tested using the Spyder IDE on Linux  dns(vegaseat)  9jul2026
'''

from PIL import Image

# open an image file (.bmp .jpg .png .gif)
# that is in the working folder or give the full path
#image_file = "../image/Flowers.jpg"
image_file = "../image/Vegaseat94.png"

img = Image.open(image_file)
# get the size of the image
width1, height1 = img.size

# set the resizing ratio so the aspect can be retained
# ratio > 1.0 increases size
# ratio < 1.0 decreases size
ratio = 0.7
width = int(width1 * ratio)
height = int(height1 * ratio)

# use one of these filter options to resize the image
# use nearest neighbour
img1 = img.resize((width, height), Image.NEAREST)
# linear interpolation in a 2x2 environment
img2 = img.resize((width, height), Image.BILINEAR)
# cubic spline interpolation in a 4x4 environment
img3 = img.resize((width, height), Image.BICUBIC)
# best down-sizing filter with newer Plllow versions
img4 = img.resize((width, height), Image.LANCZOS)

# save to file option
ext = ".png"
img1.save("NEAREST" + ext)
img2.save("BILINEAR" + ext)
img3.save("BICUBIC" + ext)
img4.save("LANCZOS" + ext)

'''
# a possible way to show the image is to activate
# the default viewer associated with the image type
import webbrowser
webbrowser.open("LANCZOS.png")
'''

# optionally show image using Tkinter ...
import tkinter as tk
from PIL import ImageTk

root = tk.Tk()
# set ULC (x, y) position of root
root.geometry("+{x}+{y}".format(x=50, y=10))
root.title('PIL different image resize options')

# convert PIL image objects to Tkinter PhotoImage objects
tk_image1 = ImageTk.PhotoImage(img1)
tk_image2 = ImageTk.PhotoImage(img2)
tk_image3 = ImageTk.PhotoImage(img3)
tk_image4 = ImageTk.PhotoImage(img4)

# display the images on labels
label1 = tk.Label(root,image=tk_image1)
label2 = tk.Label(root,image=tk_image2)
label3 = tk.Label(root,image=tk_image3)
label4 = tk.Label(root,image=tk_image4)
text1 = tk.Text(root, height=2)
text1.insert('1.0', "top to bottom: NEAREST - BILINEAR - BICUBIC - LANCZOS")

label1.pack(padx=5, pady=2)
label2.pack(padx=5, pady=2)
label3.pack(padx=5, pady=2)
label4.pack(padx=5, pady=2)
text1.pack(padx=5, pady=2)

root.mainloop()
