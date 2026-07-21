''' Button_list_tk2.py

Create a list of buttons
Show click values in an entry
Pass click() argument via lambda


tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import tkinter as tk


def click(val):
    '''
    val via lambda
    '''
    sf = "Button {} clicked".format(val)
    root.title(sf)
    entry.insert('end', val)


root = tk.Tk()
#root.geometry("{}x{}+{}+{}".format(w, h, x, y))
root.geometry("{}x{}+{}+{}".format(300, 80, 70, 100))
root.title("buttons via a list")

# only set ULC (x, y) position of root
root.geometry("+{x}+{y}".format(x=250, y=200))

# create the list of button objects
# pass click() argument via lambda
button_list = [
tk.Button(root, text=" 1 ", bg='red', command=lambda: click('1')),
tk.Button(root, text=" 2 ", bg='green', command=lambda: click('2')), 
tk.Button(root, text=" 3 ", bg='white', command=lambda: click('3'))
]

# layout the buttons horizontally with pack()
for button in button_list:
    button.pack(side='left', padx=10)

# create an entry to show button values
entry = tk.Entry(root, bg='yellow')
entry.pack(side='left', padx=3, pady=3)

root.mainloop()
