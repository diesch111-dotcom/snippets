''' Button_disable_tk2.py

A simple Tkinter app template for testing
Disable a button until text has been entered in Entry()

needs work!!

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import tkinter as tk


class MyApp(tk.Tk):
   
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("enter your name (enter key)")
        # use width x height + x_offset + y_offset (no spaces!)
        self.geometry("300x150+50+50")
        # the entry value, use self.v.get()
        self.v = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.name_entry = tk.Entry(self, textvariable=self.v)
        self.name_entry.grid(row=0, column=0, padx=10, pady=5)

        self.start_btn = tk.Button(self, text="action", state='disabled', command=self.action)
        self.start_btn.grid(row=4, column=0)
        
        # value has been entered, now enable button
        self.name_entry.bind('<Return>', self.button_enable)
        # start cursor in entry
        self.name_entry.focus()
       
    def button_enable(self, event):
        # make sure self.v is not empty
        if self.v.get():
            self.start_btn['state'] = 'normal'
    
    def action(self):
        '''do something'''
        self['bg'] = 'green'
        self.title("you entered %s" % self.v.get())
        pass


app = MyApp()
app.mainloop()
