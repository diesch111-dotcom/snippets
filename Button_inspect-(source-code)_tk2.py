#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_inspect-(source-code)_tk2.py

Since Tkinter is written in Python you can access the source code
of a specified class with Python module inspect

https://tkdocs.com/shipman/button.html

tested with LinuxMint and Spyder IDE   vegaseat  17jul2026
'''

import inspect
# python3
import tkinter as tk

root = tk.Tk()

t_btn = tk.Button(text="Hello World", width=25, bg='green')
t_btn.pack(padx=5, pady=5)

# get the Tkinter class Button source code ...
print(inspect.getsource(tk.Button))

root.mainloop()

'''
class Button(Widget):
    """Button widget."""

    def __init__(self, master=None, cnf={}, **kw):
        """Construct a button widget with the parent MASTER.

        STANDARD OPTIONS

            activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, repeatdelay,
            repeatinterval, takefocus, text,
            textvariable, underline, wraplength

        WIDGET-SPECIFIC OPTIONS

            command, compound, default, height,
            overrelief, state, width
        """
        Widget.__init__(self, master, 'button', cnf, kw)

    def flash(self):
        """Flash the button.

        This is accomplished by redisplaying
        the button several times, alternating between active and
        normal colors. At the end of the flash the button is left
        in the same normal/active state as when the command was
        invoked. This command is ignored if the button's state is
        disabled.
        """
        self.tk.call(self._w, 'flash')

    def invoke(self):
        """Invoke the command associated with the button.

        The return value is the return value from the command,
        or an empty string if there is no command associated with
        the button. This command is ignored if the button's state
        is disabled.
        """
        return self.tk.call(self._w, 'invoke')
'''