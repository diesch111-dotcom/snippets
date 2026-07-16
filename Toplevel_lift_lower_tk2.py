''' Toplevel_lift_lower_tk2.py

A tk.Toplevel() child window has options like the root window.
Size and position it with geometry()
Lift and lower it with respect to other windows.
One can exit a toplevel window alone using corner x
or it will exit as the main/root window exits.


tested using the Spyder IDE on Linux  dns aka vegaseat  15jul2026
'''

import tkinter as tk


def lift_win1():
    win1.lift(aboveThis=root)

def lower_win1():
    win1.lower(belowThis=root)


root = tk.Tk()
root.title('root win')
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("200x100+30+30")
# add color this way
root.config(bg='yellow')


# create a top/child window, can use bg color option now
win1 = tk.Toplevel(bg='red')
win1.title('top/child window = win1')
# use width x height + x_offset + y_offset (no spaces!)
win1.geometry("300x150+120+120")
# add color here
#win1.config(bg='green')

btn_lift = tk.Button(win1, text="Lift win1", command=lift_win1)
btn_lift.pack(padx=30, pady=5)
btn_lower = tk.Button(win1, text="Lower win1", command=lower_win1)
btn_lower.pack(pady=5)

print(root.keys())
print("="*40)
print(win1.keys())

win1.mainloop()

"""
['bd', 'borderwidth', 'class', 'menu', 'relief', 'screen', 'use', 
 'background', 'bg', 'colormap', 'container', 'cursor', 'height', 
 'highlightbackground', 'highlightcolor', 'highlightthickness', 'padx', 
 'pady', 'takefocus', 'visual', 'width']
========================================
['bd', 'borderwidth', 'class', 'menu', 'relief', 'screen', 'use', 
 'background', 'bg', 'colormap', 'container', 'cursor', 'height', 
 'highlightbackground', 'highlightcolor', 'highlightthickness', 'padx', 
 'pady', 'takefocus', 'visual', 'width']
"""
