''' ttk_Notebook2_images.py
A nice way to present an album of images on each notebook page

exploring the Tkinter Tile extension module ttk.Notebook()
each page gets a different picture (from GIF file)
Tkinter takes .bmp  .gif  .png (v8.6+) (image files
use PIL for .jpg

colors:
Tkinter can use a number of named colors (not case sensitive) like
red, green, blue, white, black, tan, pink, yellow, magenta, lightblue
lightgreen, moccasin, peachpuff, orange, grey, purple, brown
also (light=1 to dark=4) hues of colors like
red1, red2, red3, red4   etc.

docs
https://docs.python.org/3/library/tkinter.ttk.html
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/ttk-Notebook.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/images.html


using the Spyder IDE on Linux  dns(vegaseat) 4jul2026
'''

import tkinter as tk
import tkinter.ttk as ttk
# possible action
import os
# change the directory
# this will find eg.t'../image/any_picture.gif'
os.chdir('/media/dietrich41/9325-9047/AAtest_py/image')

root = tk.Tk()
w = 400
h = 400
x = 100
y = 50
# use width x height + x_offset + y_offset (no spaces!)
# use f_string format, new in Python3.6
root.geometry(f"{w}x{h}+{x}+{y}")
root.title('ttk.Notebook picture album')

# use .gif picture files you have
# use full path if not in working directory
pic1 = tk.PhotoImage(file='../image/Pond.gif')
pic2 = tk.PhotoImage(file='../image/Farm.gif')
pic3 = tk.PhotoImage(file='../image/House.gif')
pic4 = tk.PhotoImage(file='../image/Sunset.gif')
pic5 = tk.PhotoImage(file='../image/Oktoberfest.gif')
pic6 = tk.PhotoImage(file='../image/Ludmila.gif')
pic7 = tk.PhotoImage(file='../image/Oatis.gif')

nbk = ttk.Notebook(root)
nbk.pack(fill='both', expand='yes')

# create a child widget for each page
page1 = tk.Label(bg='blue', image=pic1)
page2 = tk.Label(bg='green', image=pic2)
page3 = tk.Label(bg='tan4', image=pic3)
page4 = tk.Label(bg='black', image=pic4)
page5 = tk.Label(bg='black', image=pic5)
page6 = tk.Label(bg='pink', image=pic6)
page7 = tk.Label(bg='brown', image=pic7)

# create the pages and name the page tabs
nbk.add(page1, text='Pond')
nbk.add(page2, text='Farm')
nbk.add(page3, text='House')
nbk.add(page4, text='Sunset')
nbk.add(page5, text='Beer')
nbk.add(page6, text='Beach')
nbk.add(page7, text='Hound')

root.mainloop()
