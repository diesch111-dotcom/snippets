#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Canvas_create_text-(XMass-snowflake_greeting)_tk2.py

animated snowflakes with holiday text message

root.update()
root.update_idletasks()
use random() and randrange() to make
lists of moves and flakes

interesting use of try/except

tested with LinuxMint and SublimeText IDE   vegaseat  17jul2026
'''

import random as rn
import tkinter as tk

root = tk.Tk()
root.title('Ho Ho Ho ...')

# create a canvas
w = 500
h = 400
cv = tk.Canvas(root, width=w, height=h, background='black')
# size of message
fnt = "Arial 20"
cv.create_text(w/2, h/2-15, text="Happy Christmas", font=fnt, fill='red')
cv.create_text(w/2, h/2+15, text="from Stew Pitt", font=fnt, fill='green')
cv.pack()

# create snow flakes and their movements
flakes = []
moves = []
# you can change the number of flakes (50)
# but animation gets sluggish with higher values
for k in range(50):
    # size of '*' snow flakes
    fnt = "Times 30"
    flakes.append(cv.create_text(rn.randrange(w), rn.randrange(h),
                                text="*", fill='white', font=fnt))
    moves.append([0.04 + rn.random()/10, 0.7 + rn.random()])

# eventloop and animation redraw
try:
    while True:
        for x in range(len(flakes)):
            p = cv.coords(flakes[x])
            p[0] += moves[x][0]
            p[1] += moves[x][1]
            cv.coords(flakes[x], p[0], p[1])
            if p[1] > h+10:
                cv.coords(flakes[x], rn.randrange(w), -10)
            root.update_idletasks()  # redraw
            root.update()  # process events
except:
    pass
 
