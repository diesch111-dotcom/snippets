#!/usr/bin/env python3
# -*- coding: utf-8 -*
''' Button_expanded_event_handler_tk2.py

Expanding the event handler for a tk.Button()
to pass other values with the event

uses a class

mouse clicks:
'<Button-1>' = left mouse click/press, same as '<ButtonPress-1>' or '<1>'

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("expanded event handler")
        # use width x height + x_offset + y_offset (no spaces!)
        self.geometry("340x220+50+50")
        self['bg'] = 'green'
        self.createWidgets()

    def createWidgets(self):
        """
        create a series of buttons
        and assign an expanded event handler
        """
        for k in range(1, 7):
            btn_text = "button{}".format(k)
            btn = tk.Button(self, text=btn_text)
            btn.pack(pady=5)
            # expanded event handler now contains the button label
            # could be other values too
            def handler(event, self=self, label=btn_text):
                return self.btn_clicked(event, label)
            # respond to left mouse click
            btn.bind('<1>', handler)

    def btn_clicked(self, event, label):
        """action code when button is clicked"""
        s = "you clicked button: {}".format(label)
        self.title(s)
        print(s)
        

app = MyApp()
app.mainloop()
