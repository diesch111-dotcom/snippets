#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Canvas_class_drawings_circle_tk2.py

A Tkinter class template for canvas drawings

tk.Canvas()
canvas.create_oval()
given center and radius get the bounding box via get_square()

to draw a circle you need to get the upper left
and lower right corner coordinates of a square
draw the circle that fits into the square
size = 100
x = 120
y = 120
ULC = upper_left_corner_coordinates = (x, y)
LRC = lower_right_corner_coordinates = (x+size, y+size)
rect = (ULC, LRC)
circle = cv.create_oval(rect)

def get_square(x, y, radius):
    """
    given the center=(x, y) and radius
    calculate the square for a circle to fit into
    return x1, y1, x2, y2 of the square's ulc=(x1, y1) and
    lrc=(x2, y2) diagonal corner coordinates
    """
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    return x1, y1, x2, y2

see also
https://tkdocs.com/shipman/

tested using the Spyder IDE on Linux  vegaseat  4jul2026
'''

# for Python2 uses Tkinter
import tkinter as tk


class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("explore canvas drawing (click mouse)")
        self.create_canvas()
        # draw_circle(x, y, size, color)
        self.circle1 = self.draw_circle(120, 120, 150, 'yellow')
        # draw another circle
        self.circle2 = self.draw_circle(150, 150, 170)

    def create_canvas(self):
        # create a canvas to draw on
        self.cv = tk.Canvas(self, width=400, height=400, bg='white')
        self.cv.grid()
        # optional left mouse button action on canvas click
        self.cv.bind("<Button-1>", self.action)

    def draw_circle(self, x, y, size, color=None):
        '''
        a circle is drawn in a square box
        default outline color is black
        '''
        # create a square box with upper left corner (x,y)
        box = (x, y, x + size, y + size)
        # create a circle that fits the box
        return self.cv.create_oval(box, fill=color, outline='black')

    def action(self, event, tog=[0]):
        # toggles between True=1 and False=0
        tog[0] = not tog[0]
        print(tog[0])   # test
        if tog[0] == True:
            self.draw_circle(150, 150, 170, 'pink')
        else:
            self.draw_circle(150, 150, 170, 'magenta')
        pass

    def run(self):
        '''get the event mainloop going'''
        self.mainloop()


MyApp().run()

