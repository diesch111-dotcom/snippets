''' canvas_create_line_plotting_tk102.py

plot a basic graph using Tkinter cavas.create_line()
and a list of continous x,y points for the line
x increments by 1 and y=sin(x) in sin_list corresponding
cos_list has x and cos(x) values

tk.Canvas()
canvas.create_line()

could be fancied up with value markers on the y and x axis 

some info at
https://docs.python.org/3/library/tkinter.html

curious fact:
in the LinuxMint terminal type:  python3 -m tkinter
to get a small tkinter window showing the version of tkinter you have

tested with LinuxMint and Spyder IDE  dns aka vegaseat  19jun2026
'''

# for math.sin() and math.cos() values
import math
import tkinter as tk

root = tk.Tk()
root.title("canvas.create_line() sin/cos basic plotting")
width = 400
height = 300
center = height//2
x_increment = 1
# width stretch
x_factor = 0.04
# height stretch
y_amplitude = 80

# create a canvas to draw on root window will expand to fit canvas
cv = tk.Canvas(width=width, height=height, bg='white')
cv.pack()

# create the continuous x,y points list for the sin() curve
# (values have to be integers)
sine_list = []
for x in range(width):
    # x coordinates
    sine_list.append(x * x_increment)
    # y coordinates
    sine_list.append(int(math.sin(x * x_factor) * y_amplitude) + center)

#print(sine_list)  # test

# create the coordinate list for the cos() curve
cos_list = []
for x in range(width):
    # x coordinates
    cos_list.append(x * x_increment)
    # y coordinates
    cos_list.append(int(math.cos(x * x_factor) * y_amplitude) + center)

# do the Tkinter canvas drawings
s = "sin(x)=blue  cos(x)=red"
cv.create_text(10, 20, anchor='sw', text=s)
center_line = cv.create_line([0, center, width, center], fill='black')
# application of sine_list is interesting, continuous x,y points
sin_line = cv.create_line(sine_list, fill='blue')
cos_line = cv.create_line(cos_list, fill='red')

# change the thickness/width of the sin/cos lines to 2 pixels
# this width is not the width of the canvas
cv.itemconfig(sin_line, width=2)
cv.itemconfig(cos_line, width=2)

root.mainloop()
