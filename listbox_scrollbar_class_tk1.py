''' listbox_scrollbar_class_tk1.py

A ScrolledListbox class for general application 
has vertical and horizontal scrollbars

https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/


using the Spyder IDE on Linux  dns aka vegaseat 4jul2026
'''

import tkinter as tk


class ScrolledListbox(tk.Frame):
    def __init__(self, *args, **kwds):
        tk.Frame.__init__(self,  *args, **kwds)
        self._create_gui(**kwds)

    def _create_gui(self, width=35, height=20, **kwds):
        "give width and height some default values"
        print(width, height)  # test
        self.listbox = tk.Listbox(self, width=width, height=height, **kwds)
        self.listbox.grid(row=1, column=1, sticky="nsew")
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
# long enough to activate the vertical and horizontal scrolls
# the laat item is some sort of a ruler
itemslist = [
'Stew', 'Tom', 'Jen', 'Adam', 'Ethel', 'Barb', 'Tiny', 'Asta',
'and now an extended string to activate the horizontal scrolling',
'Tim', 'Pete', 'Sue', 'Egon', 'Fuzzy', 'Swen', 'Albert', 'Zoey',
'123456789_123456789_123456789_123456789__123456789_']


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scrolled Listbox")
    frame = ScrolledListbox(root, width=40, height=12)
    frame.grid()
    # load the listbox
    for item in itemslist:
        frame.listbox.insert("end", item)

    root.mainloop()
    
