''' slide_show_images_folder_tk2.py

A simple Tkinter slide show using glob and PIL.
Goes through the .gif .png and .jpg files of a given folder.
Uses an endless cycle unless you double click on the picture.

Ideally, put this little Python program right into the folder that contains 
the picture images you want to show!  

On a Linux terminal use ...
sudo apt-get install python3-pillow
to install pillow if needed

Even though you install pillow, you still use the PIL namespace 
in your Python code.

tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import os
import glob
# PIL allows display of .jpg .png .bmp and .gif files
from PIL import ImageTk
from itertools import cycle
import tkinter as tk

root = tk.Tk()
# set root ULC (x, y) position
root.geometry('+{}+{}'.format(50, 100))


def show_slides():
    '''cycle through the images and show them'''
    img_object, img_name = next(pictures)
    # show the image in the label
    label_pict["image"] = img_object
    # show the filename in the title
    root.title(img_name)
    # optional testing...
    s3 = f'{img_name}  {img_object.width()}x{img_object.height()}'
    print(s3)  # test
    # delay for a number of milliseconds
    root.after(delay, show_slides)

def exit(event):
    "exit the program"
    print('Go, going, gone ...')
    root.destroy() 


# use the current working directory or specify another image directory
directory = os.getcwd()
#directory = "../image"
os.chdir(directory)
# a good way to use module glob
# create a list of all .jpg .png and .gif files in the given directory
img_files = glob.glob("*.jpg") + glob.glob("*.png") + glob.glob("*.gif")

# optionally sort the list of filenanmes 
img_files.sort(key=str.lower)

# milliseconds to show each image
delay = 2000

# allows cycling through the pictures
# are (img_object, img_name)) tuples
pictures = cycle((ImageTk.PhotoImage(file=image), image)
                for image in img_files)
# create the label to show the pictures in
# label expands ro fit image
label_pict = tk.Label(root)
# mouse double click on label image to exit
label_pict.bind('<Double-1>', exit)
label_pict.pack()

# function helps to exit smoother
show_slides()

root.mainloop()
