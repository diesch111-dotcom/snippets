''' askstring_simpledialog_tk1.py

Use Tkinter's simpledialog to ask for user input.
The dialogs are askfloat, askinteger, and askstring.
Expects you to enter a float, an integer or a string respectively
and will prompt until correct.

initialvalue, minvalue and maxvalue are optional
if you enter an integer, it will be converted to a float
tksd.askfloat(title, prompt, initialvalue=None,
    minvalue=None, maxvalue=None, parent=None)

accepts integers only (char 0 to 9 and -+) 
has to be an integer value or it will keep aaking  
tksd.askinteger(title, prompt, initialvalue=None,
    minvalue=None, maxvalue=None, parent=None)

tksd.askstring(title, prompt, initialvalue=None)
initialvalue can be used to show a short result too

docs
https://docs.python.org/3/library/dialog.html
https://tkdocs.com/shipman/message.html
https://tkdocs.com/shipman/tkMessageBox.html
https://docs.python.org/3/library/tkinter.html

Again, simple dialogs are:
askfloat(), askinteger(), and askstring()

messagebox dialogs are:
showinfo(), showwarning(), showerror(), askquestion(), 
askokcancel(), askyesno(), askretrycancel()


# there is also module turtle within tkinter
import turtle as tu
tu.Screen().setup(15, 15)
# string input
#str1 = tu.textinput(title, prompt)
name = tu.textinput("Name", "Please enter your name:")
# float input, integer value converted to float
#num1 = tu.numinput(title, prompt, default=None, minval=None, maxval=None)
age = tu.numinput("Age", "How old are you:", minval=0, maxval=150)


using LinuxMint with Python3 and Python3-tk installed
works nicely with Sublime and Spyder IDE
dns aka vegaseat  25apr2026
'''

# Python3
import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.simpledialog as tksd


root = tk.Tk()
# show askstring dialog without the Tkinter window showing
root.withdraw()

# (title, prompt)
# returns a string
# can also be used to display a short result string
name = tksd.askstring("Name", "Enter your name:")
# accepts scientific notations eg. 1.2e6 returns a float
cost = tksd.askfloat("Cost", "Amount you spend on food/day:")
# accepts and returns an integer (char 0 to 9 and -+) no 1e3 for 1000
days = tksd.askinteger("Days", "How many days are you staying here?")


# don't exceed the text line length the messagebox can handle
result_str = f"""\
Thank you {name}.
You might spend ${cost:0.2f} on food 
per day, and you will be here for 
another {days} days.
"""

# you can use askstring to display a short one line result
#msg = "{}\' cost = ${:0.2f}".format(name, cost * days)
tksd.askstring("Result", "Total food cost is: ", initialvalue=cost * days)

# use a messagebox for a multiple line result
hey = tkmb.showinfo("Oh dear!", result_str)

# optional ...
#help(tksd)
#help(tkmb)
#help(tkmb)