#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" colorchooser_tk2.py

explore the Tkinter colorchooser dialog
the final adjusted color will display on the console window as a
rgb_tuple (r, g, b) and a hexstring '#rrggbb'
copy/paste the hexstring to your tkinter code
tkinter will not take color tuples

tested using the Sublime IDE on Linux  dns(vegaseat)  8jul2026
"""

import tkinter as tk
import tkinter.colorchooser as cc


class ColorPick(object): 
    def __init__(self, root): 
        self.frame = tk.Frame(root) 
        self.frame.pack(padx=5, pady=5, anchor='nw', expand=True, 
            fill='both')
    
        self.labelframe = tk.LabelFrame(self.frame, 
                                        text='Click on a strip below') 
        self.labelframe.pack(padx=2, pady=2, expand=True, 
            fill='both')
        # initial three colors
        self.colors = ['pink', 'lime', 'gold']
        # create three canvases via list comprehension
        self.canvases = [tk.Canvas(self.labelframe,# width=60, 
            height=22, background=col) for col in self.colors] 

        for ix, cv in enumerate(self.canvases): 
            cv.bind("<Button-1>", 
                lambda e, ix=ix: self.choose_color(ix)) 
            cv.pack(padx=2, pady=4, anchor=tk.NW)
        
        self.text1 = tk.Text(self.labelframe, font=['Arial', 16]) 
        self.text1.pack()


    def choose_color(self, ix):
        """
        Click on one of the color stripes to bring up the colorchooser
        dialog.  Use the Red, Green, Blue sliders to adjust the color,
        then click the OK button. That will return the new color in the
        form of a rgb_tuple (r, g, b) and a hexstr '#rrggbb' to display
        on the console.  Copy/Paste the hexstr for use in tkinter code.
        """
        rgb_tuple, hexstr = cc.askcolor(color=self.colors[ix]) 
        # color info to console for testing...
        print('colorchooser returned {} {}'.format(rgb_tuple, hexstr))
        # one can also highlight, then copy ctrl/c and paste ctrl/v from 
        # a Text widget
        # the start of line 1 is indexed as '1.0' (means 'row.column')
        self.text1.insert('1.0', hexstr + '\n')
        # update the canvases
        if hexstr: 
            self.canvases[ix].config(background=hexstr) 
            self.colors[ix] = hexstr

      
# test class ColorPick ...
if __name__ == '__main__':

    root = tk.Tk()
    # set the root window's height, width and x,y position
    # x,y are the upper left corner coordinates in pixels
    w = 300
    h = 230
    x = 50
    y = 100
    # use width x height + x_offset + y_offset (no spaces!)
    root.geometry("{}x{}+{}+{}".format(w, h, x, y))
    root.title('colorchooser')
    
    ColorPick(root)
    
    root.mainloop() 
    