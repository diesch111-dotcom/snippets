
''' mouse_wheel_tk2.py

Explore the mouse wheel with Tkinter

tested with LinuxMint and Spyder IDE   vegaseat  17jul2026
'''

import tkinter as tk


def mouse_wheel(event):
    global counter
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        counter -= 1
    if event.num == 4 or event.delta == 120:
        counter += 1
    label['text'] = counter
    str = "root wheel count = {}".format(counter)
    root.title(str)
    print(str)

counter = 0
root = tk.Tk()
root.title('turn mouse wheel')
root['bg'] = 'darkgreen'
root['cursor'] = 'hand1'

# Windows
root.bind("<MouseWheel>", mouse_wheel)
# Linux
root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)

label = tk.Label(root, font=('courier', 18, 'bold'), width=10)
label.pack(padx=70, pady=40)

root.mainloop()
