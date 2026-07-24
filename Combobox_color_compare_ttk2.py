''' Combobox_color_compare_ttk2.py

exploring the ttk.Combobox() and its actions
allows one item to be selected

compare colors that are close next to each other

similar to tk.OptionMenu()

Tkinter can use a number of named colors (not case sensitive) like
red, green, blue, white, black, tan, pink, yellow, magenta, lightblue
lightgreen, moccasin, peachpuff, orange, grey, purple, brown
also (light=1 to dark=4) hues of colors like
red1, red2, red3, red4   etc.

tk has also color format hex "#rrggbb" for instance:
azure = '#f0ffff'
beige = '#f5f5dc'
bisque = '#ffe4c4'
chocolate = '#d2691e'
gainsboro = '#dcdcdc'
gold = '#ffd700'
thistle = '#d8bfd8'

see: color_dictionary_list1.py

Python27+ includes the Tkinter Tile extension Ttk.
Ttk comes with 17 widgets, 11 of which already exist in Tkinter:
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton,
PanedWindow, Radiobutton, Scale and Scrollbar
The 6 new widget classes are:
Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview


works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
'''

import tkinter as tk
import tkinter.ttk as ttk


def show_selection1(event=None):
    '''
    use the selected color to color the frame1 background ('bg')
    '''
    # can also use var1.get()
    color = combo1.get()
    frame1['bg'] = color

def show_selection2(event=None):
    '''
    use the selected color to color the frame2 background ('bg')
    '''
    # can also use combo2.get()
    color = var2.get()
    frame2['bg'] = color

root = tk.Tk()
# only set size of root
w = 600
h = 300
root.geometry("{}x{}".format(w, h))
#root['bg'] = 'green'
root.title('ttk.Combobox() select close colors')

frame1 = tk.Frame(width=600, height=300)
frame1.pack(side='top', fill='both', expand='yes')
frame2 = tk.Frame(width=600, height=300)
frame2.pack(side='top', fill='both', expand='yes')

close_choices = [
    'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4',
    'azure', 'azure1', 'azure2', 'azure3', 'azure4',
    'bisque', 'bisque1', 'bisque2', 'bisque3', 'bisque4',
    'blue', 'blue1', 'blue2', 'blue3', 'blue4',
    'brown', 'brown1', 'brown2', 'brown3', 'brown4',
    'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4',
    'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4',
    'coral', 'coral1', 'coral2', 'coral3', 'coral4',
    'cornsilk', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4',
    'gold', 'gold1', 'gold2', 'gold3', 'gold4', 
    'green', 'green1', 'green2', 'green3', 'green4',
    'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'orange', 'orange1', 'orange2', 'orange3', 'orange4', 
    'pink', 'pink1', 'pink2', 'pink3', 'pink4',
    'red', 'red1', 'red2', 'red3', 'red4',
    'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4',
    'snow', 'snow1', 'snow2', 'snow3', 'snow4',
    'red', 'red1', 'red2', 'red3', 'red4',
    'tan', 'tan1', 'tan2', 'tan3', 'tan4', 
    'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 
    'tomato', 'tomato1', 'tomato2', 'tomato3', 'tomato4', 
    'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4',
    'yellow', 'yellow1', 'yellow2', 'yellow3', 'yellow4', 'yellowGreen',
    'wheat', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white', 'whiteSmoke']

var1 = tk.StringVar(root)

#choices1 = ['red', 'green', 'blue', 'yellow', 'orange', 'white']
choices1 = close_choices
combo1 = ttk.Combobox(frame1, textvariable=var1, values=choices1)
combo1.bind("<<ComboboxSelected>>", show_selection1)
# default is pack from top down
combo1.pack(pady=45, padx=20)

var2 = tk.StringVar(root)
# initial valuel
var2.set('tan')

#choices2 = ['red4', 'lightgreen', 'lightblue', 'pink', 'brown', 'tan']
choices2 = close_choices
combo2 = ttk.Combobox(frame2, textvariable=var2, values=choices2)
combo2.bind("<<ComboboxSelected>>", show_selection2)
# default is pack from top down
combo2.pack(pady=45, padx=20)

# initial value
combo1.set('azure')
show_selection1()
combo2.set('azure')
show_selection2()

# optional
sz = ttk.Sizegrip()
sz.pack(anchor='se')

root.mainloop()
