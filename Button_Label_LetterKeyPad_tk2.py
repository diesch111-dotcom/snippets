''' Button_Label_LetterKeyPad_tk1.py

Create an upper case letter key pad with Tkinter to enter text.
Create and position all buttons with a for-loop.

docs
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/labelframe.html
https://tkdocs.com/shipman/entry.html
https://tkdocs.com/shipman/grid.html


tested using the Spyder IDE on Linux  dns aka vegaseat  13jul2026
'''

from functools import partial
import tkinter as tk


def click(btn):
    """
    button command click value via partial function
    """
    enter.insert('end', btn)
    print(btn)  # testing,,,


root = tk.Tk()
root['bg'] = 'blue'
root.title("Letter Keypad to type")

# create a labeled frame for the keypad buttons
# relief='groove' and labelanchor='nw' are default
lf = tk.LabelFrame(root, text=" Letter Keypad ", bd=3)
lf.pack(padx=15, pady=10)

# from string.uppercase
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# create and position all buttons with a for-loop
# r, c used for row, column grid values
r = 1
c = 0
n = 0
# list(range()) needed for Python3
btn = list(range(len(letters)))
for letter in letters:
    # partial takes care of function and argument
    cmd = partial(click, letter)
    # create the button
    btn[n] = tk.Button(lf, text=letter, width=5, command=cmd)
    # position the button
    btn[n].grid(row=r, column=c)
    # increment button index
    n += 1
    # update row/column position
    c += 1
    if c > 4:
        c = 0
        r += 1

# create a display
enter = tk.Entry(root, width=33, bg="yellow")
enter.pack(padx=15, pady=10)

root.mainloop()
