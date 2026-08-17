#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' listbox_scrollbar_class_tk1.py

A ScrolledListbox class for general application 
has vertical and horizontal scrollbars triggered on demand

https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/

tested with IDLE IDE on LinuxMint  VegasEat 19jul2026
'''

import tkinter as tk


class ScrolledListbox(tk.Frame):
    def __init__(self, *args, **kwds):
        tk.Frame.__init__(self,  *args, **kwds)
        self._create_gui(**kwds)

    def _create_gui(self, width, height, **kwds):
        self.listbox = tk.Listbox(self, width=width, height=height, **kwds)
        self.listbox.grid(row=1, column=1, sticky="nsew", padx=5)
        self.scrollx = tk.Scrollbar(self, orient="horizontal", 
                                    command=self.listbox.xview)
        self.scrollx.grid(row=2, column=1, sticky="ew")
        self.scrolly = tk.Scrollbar(self, orient="vertical", 
                                    command=self.listbox.yview)
        self.scrolly.grid(row=1, column=2, sticky="ns")
        self.listbox.config(xscrollcommand=self.scrollx.set, 
                            yscrollcommand=self.scrolly.set)
        # use left mouse click on a list item to display selection
        self.listbox.bind('<ButtonRelease-1>', self.on_click_listbox)

    def on_click_listbox(self, event):
        # get selected line index
        index = self.listbox.curselection()
        # get the line's text
        seltext = self.listbox.get(index)
        # for testing show in title
        root.title(seltext)


# create a list of items to put into the listbox
# long and wide enough to trigger the vertical and horizontal scrolls
arduino_sensor_list = ['DHT11 temperature and humidity sensor module',
 'HC-SR501 infrared human body induction module',
 'DS1302 real time clock module',
 'The rain sensor module for outdoor use',
 'Sound sensor module with microphone',
 'HC-SR04 ultrasonic sensor',
 'The industrial grade flame sensor module',
 'KY-008 laser head sensor/emitter module',
 'CdS Photo sensitive resistance sensor module',
 'The YL-69 soil moisture sensor',
 'IR obstacle avoidance sensor',
 'Vibration sensor module',
 'MQ-2 gas sensor module',
 '315M super regenerative receiver module',
 'The tilt sensor module',
 'The all time famous robot special low price path tracing module']


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Arduino sensor sale...")
    frame = ScrolledListbox(root, width=40, height=12, bg="wheat")
    frame.grid()
    # load the listbox
    for item in arduino_sensor_list:
        frame.listbox.insert("end", item)

    root.mainloop()
    
