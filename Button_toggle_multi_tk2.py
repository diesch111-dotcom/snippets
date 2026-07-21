#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Button_toggle_multi_tk2.py

Test various ways to toggle a tkinter button

docs
https://tkdocs.com/shipman/button.html
https://docs.python.org/3/library/itertools.html

tested with LinuxMint and Spyder IDE  vegaseat  20jul2026
'''

import itertools
# Python3
import tkinter as tk


def toggle1(tog=[0]):
    '''
    a list default argument has a fixed address
    '''
    tog[0] = not tog[0]
    # cycles through True and False
    t_btn1.config(text='False') if tog[0] else t_btn1.config(text='True') 

def toggle2(icycle=itertools.cycle([False, True])):
    '''
    cycles through True and False
    '''
    state = next(icycle)
    t_btn2['text'] = str(state)

def toggle3(icycle=itertools.cycle(['yellow', 'aqua', 'lime', 'tan'])):
    '''
    cycles through the list of colors
    '''
    color = next(icycle)
    print(color)
    t_btn3['bg'] = color


root = tk.Tk()
# width x height in  pixels
root.geometry('300x130')
root.title('testing toggle buttons')
root['bg'] = 'pink'

t_btn1 = tk.Button(root, text="True", width=12, command=toggle1)
t_btn2 = tk.Button(root, text="True", width=12, command=toggle2)
t_btn3 = tk.Button(root, text="color toggle", width=12, command=toggle3)

# pack() default is center from the top first
t_btn1.pack(pady=5)
t_btn2.pack(pady=5)
t_btn3.pack(pady=5)

root.mainloop()
