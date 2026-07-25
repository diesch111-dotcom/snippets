#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Canvas_ButtonImageb64_text_tk2.py
a base64 encoded GIF image string is simple to use with Tkinter
use it for an image to put text on

canvas has no bind()

Can also put the image data on a tk.Button(), now you can action push

docs
https://tkdocs.com/shipman/images.html

tested using the Spyder IDE on Linux  vegaseat  4jul2026
'''

import tkinter as tk

# base64 encoded GIF image string (without the text)
# created with Base64encGIF_py23.py
bt_yellow_oval_gif_b64='''\
R0lGODlhmwAjAPcAAAcFBoSFBIWFhkZEBcTGlEpFTcXEBMPDxCQkBGNkBMzSTKakhmRiUSooOUZE
MZCMROTmBOnkyKSkrOTokKalBDU0BVRUBGRmdNziLFZUUeTk5BcUBGZkQpOUhOTmTPP1BVdTL+Ti
tCUkI7Szh7KzrFxVZOzufISDOcTCNM7SynJ1BMnFrHh4WKSkLDg1HBsVHdTUBEI+TlRSHL69xEVE
Ifz4yEREQ6yuTJaVBDo4ObW0BJSVntnUt3l4eLu8s6SkoV5bUvz0GPL06C0sCIyKZB0bBfv+pczN
12VkZPb5SkxDX2RjH+jrBPv5h1xbBj88IIyMiExMB/z+a9DMrz89RPT1uQwGHMnMyZ+cifz7CS4s
HnR5H3h4hPT0WLzCHNzi3PT4KNPT1dbaBPz+eQ4MCE9NMVRTP7q1n2FdZj0+OryyFPT09JSUfIeL
GU5MTczNBGtsBLGsij07CFlVXHZ1MLW1vHp7BHV0aff02E1MQ4yUGPT6nOzyPO7rzKSmHBUUFL68
BMTCbKyueNzejJSSNNzeLNjYfJyYSLSyNISGXIWFe25vQHRxdY6MMh0cHZ2cnby+TNzapGxrUezy
mOzuVDQxNKyqBPTuJOTexF5cHPPt1ImLBK2sruvs615eMO7rtlBNHJucBN7cvKyuofv+6mxsalRM
YHBsINvc219dPL+8ofz82JyeHPz+Nby6fLm3lKyqNBQOLJSSVMfNMfz+GPz8uPz+WPz8/JyeLKGd
fMTDpCckFGRiFJyilOTjFFRSFJSTlL/DvDQ0LLy8vB4dFOjsFFxbFD48LIyNlExKFMTKvJ6clNze
FHh8FHRyhISGlEhFFGZlXDUyFComLHRyFEQ6XF1bXDItFCwsLBQOFGRcdLKulDw+FBwaLJyerOTq
nOTiXGxuXIR+XH1+ePz+RYF+h/z+Jo6KetTGFLy6jPT2dPz+hnl6bPr+mXR2PKSqKLy6HMTGDMXE
zCckDGRiDOTmDKymDFdVDBgSDJaUjLS0tGBWbL7CtDAyJNTSDFNVJCH5BAAAAAAALAAAAACbACMA
Bwj/AIMNu6Iv2AyBda7MmFEnzIxbt4RoQEWx05o1YYZx+sFR3wFUFjtp0CByIsk1t9Z0EokqjEJ9
GzkNDAPSYsqJnVKunBjmwDB9QIFufET00Q8JnPT5CHogzBeRNiGqpEhTw0WRV+qMOpo0GB4hpIR8
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
AQA7
'''
    

root = tk.Tk()
root.title("display a base64 encoded gif image")

def action():
    print('pinko')
    cv['bg'] = 'pink'

photo = tk.PhotoImage(data=bt_yellow_oval_gif_b64)

# create a white canvas
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')

# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
xpos = 50
ypos = 30
# cannot bind this or a canvas
cv.create_image(xpos, ypos, image=photo, anchor='nw')
# put some text on the canvas image
sa = "Hello there!"
cv.create_text(xpos+20, ypos+10, anchor='nw', text=sa)

# however you can bind/command this button
button = tk.Button(cv, image=photo, command=action)
button.place(x=xpos, y=ypos+40)

root.mainloop()
