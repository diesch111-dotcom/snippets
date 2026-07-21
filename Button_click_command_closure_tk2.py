''' Button_click_command_closure_tk2.py

Using a closure to pass command click arguments

docs
https://tkdocs.com/tutorial/index.html
https://tkdocs.com/shipman/button.html
https://docs.python.org/3/library/tkinter.html

curious fact:
in the LinuxMint terminal type:  python3 -m tkinter
to get a small tkinter window showing the version of tkinter you have

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import tkinter as tk


def click(name):
    """a typical closure, a function within a function"""
    def inner_click():
        s = "Button {} clicked via 'closure'".format(repr(name))
        root.title(s)
        print(s)
    return inner_click


root = tk.Tk()
root.title("click any of the buttons")
# background color of the root window
root['bg'] = 'green'

b1 = tk.Button(text="one", width=10, command=click("one"))
b2 = tk.Button(text="two", width=10, command=click("two"))

# pack default is center from top first
b1.pack(padx=150, pady=10)
b2.pack(pady=5)

root.mainloop()
