''' Button_activebackground_click_color_tk2.py

Set activebackground of the button to momentarily change color
when clicked

Tkinter can use a number of named colors (not case sensitive) like
red, green, blue, white, black, tan, pink, yellow, magenta, lightblue
lightgreen, moccasin, peachpuff, orange, grey, purple, brown
also (light=1 to dark=4) hues of colors like
red1, red2, red3, red4   etc.

docs
https://tkdocs.com/shipman/button.html
https://tkdocs.com/shipman/colors.html

curious fact:
in the LinuxMint terminal type:  python3 -m tkinter
to get a small tkinter window showing the version of tkinter you have

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import tkinter as tk


def show_pressed(btn): 
    btn.config(activebackground='red') 

  
root = tk.Tk()
# set width x height
root.geometry("320x40")
root.title("click any of the buttons")
# background color of the root window
root.config(bg='beige')

btn1 = tk.Button(root, text='Button1', bg='yellow') 
# change button color when pressed, procedure 1
btn1.bind('<ButtonPress-1>', lambda event: show_pressed(btn1))

# change button color when pressed, procedure 2 (simpler)
btn2 = tk.Button(root, text='Button2', activebackground='cyan',
        bg='green')

# change button color when pressed, procedure 2 (simpler)
btn3 = tk.Button(root, text='Button3', activebackground='lime',
        bg='blue')

# pack() default is center from top first
# or left to right here
btn1.pack(side='left', padx=5, pady=5) 
# this button will be next right to btn1
btn2.pack(side='left', padx=5, pady=5) 
# this button will be next right to bnt2
btn3.pack(side='left', padx=5, pady=5) 

root.mainloop() 
