''' ttk_Notebook2_texts.py
A nice way to read a developing story via a ttk.Notebook one page at a time

exploring the Tkinter Tile expansion module ttk.Notebook()

ttk comes with 17 widgets, 11 of which already exist in Tkinter:
Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton,
PanedWindow, Radiobutton, Scale and Scrollbar

The 6 new widget classes are:
Combobox, Notebook, Progressbar, Separator, Sizegrip and Treeview

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/ttk-Notebook.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/frame.html


using the Spyder IDE on Linux  dns(vegaseat) 4jul2026
'''

import tkinter as tk
import tkinter.ttk as ttk

text1 = """\
A priest was talking to a nun, and he saw that
her belly was getting noticeably big, and
he made a comment about it.  She replied to
him that it was just a little gas. 
"""

text2 = """\
A couple months later, he ran into her again.
This time, her belly was really big. She just
patted her belly and said, "Just a little gas."
"""

text3 = """\
Two months went by, and he came across the
nun again, and she was pushing a baby carriage.  
The priest bent down and looked into the
carriage and said, "Cute little fart, isn't he?"
"""

    
root = tk.Tk()
# adjust the root widrh so the texts fit
w = 560
h = 200
x = 100
y = 50
# use width x height + x_offset + y_offset (no spaces!)
# use f_string format, new in Python3.6
root.geometry(f"{w}x{h}+{x}+{y}")
root.title('ttk.Notebook story reader')

nbk = ttk.Notebook(root)
nbk.pack(fill='both', expand='yes')

# create a child widget for each page
# allign the text to the left side
page1 = tk.Label(bg='wheat', text=text1, font=['Arial', 16], 
                 justify=tk.LEFT, padx=10)
page2 = tk.Label(bg='wheat', text=text2, font=['Arial', 16], 
                 justify=tk.LEFT, padx=10)
page3 = tk.Label(bg='wheat', text=text3, font=['Arial', 16], 
                 justify=tk.LEFT, padx=10)

# create the pages and name the page tabs
nbk.add(page1, text='Beginning')
nbk.add(page2, text='Middle')
nbk.add(page3, text='Finale')


root.mainloop()
