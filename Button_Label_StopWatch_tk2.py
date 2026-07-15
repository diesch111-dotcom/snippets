#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_Label_StopWatch_tk2.py

A basic Tkinter Stopwatch using... 
tk.Button()
tk.Label()
.after() and .after_cancel().

Could add reset()

in the Linux terminal type:  python3 -m tkinter
to get a small tkinter window showing the version of tkinter


tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

import tkinter as tk


class StopWatch(tk.Tk):
    def __init__(self):
        # root = self
        tk.Tk.__init__(self)
        self.title("A Simple Tkinter Stopwatch")
        # use width x height + x_offset + y_offset (no spaces!)
        self.geometry("370x50+20+50")
        self.create_widgets()

    def create_widgets(self):
        myfont = ('Comic Sans MS', 24, 'bold')
        self.btn_start = tk.Button(self, text="Start", font=myfont,
            command=self.start)
        self.btn_start.grid(row=0, column=0, padx=5, pady=5)

        self.btn_stop = tk.Button(self, text="Stop", font=myfont,
            command=self.stop)
        self.btn_stop.grid(row=0, column=1)

        self.label = tk.Label(self, fg='red', font=myfont)
        self.label.grid(row=0, column=3, padx=5)

    def start(self, sec=[-1]):
        # accumulate seconds using list default arg
        sec[0] += 1
        self.label.config(text="{:5d} seconds".format(sec[0]))
        # .after() calls itself every 1000 ms = 1 second
        self.id = self.btn_start.after(1000, self.start)

    def stop(self):
        # use of .after_cancel()
        self.btn_start.after_cancel(self.id)

    def run(self):
        '''get the event mainloop going'''
        self.mainloop()


StopWatch().run()
