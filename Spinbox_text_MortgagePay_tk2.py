#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' Spinbox_text_MortgagePay_tk2.py

Use 3 tk.Spinbox() to enter interest, years and principle loan
Calculate monthly mortgage as data is changed and display the
result in tk.Text() having a vertical scrollbar

For mortgage payments use ... 
# monthly interest rate given % annual interest
interest_rate = interest/(100 * 12)
# total number of payments
payment_num = years * 12
# calculate monthly payment
payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))

docs
https://tkdocs.com/shipman/spinbox.html
https://tkdocs.com/shipman/text.html
https://tkdocs.com/shipman/scrollbar.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/universal.html

tested using the SublimeText IDE on Linux  vegaseat  4jul2026
'''

import math
import tkinter as tk

root = tk.Tk()
# width x height
root.geometry('480x400')
#root.resizable(False, False)
root.title('Monthly Mortgage Payments')


def value_changed(event=None):
    '''
    value1.get() is a string so is spin_box1.get()
    since tk.Spinbox() textvariable is used?
    '''
    # % annual interest
    interest = float(spin_box1.get())
    # monthly interest rate given % annual interest
    interest_rate = interest/(100 * 12)
    years = int(spin_box2.get())
    # total number of payments given years
    payment_num = years * 12
    principal = int(spin_box3.get())
    # calculate monthly payment
    payment = principal * \
             (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
    total = payment * years * 12
             
    sf1 = '${:.2f}/month for a loan of ${:,} \n'
    sf2 = 'at {}% annual interest over {} years\n'
    sf3 = 'total paid = ${:,.2f}\n\n'
    sf4 = sf1 + sf2 + sf3 
    result = sf4.format(payment, principal, interest, years, total)
    print(result)
    text1.insert('end', result)
    text1.see('end')

    
root.bind("<Return>", value_changed) 
  
# side='top' centers widthwise
pack_dict = {'side': 'top', 'padx': 5, 'pady': 2}

myfont = ('courier', 20, 'bold')

label1 =tk.Label(root, text='% annual interest:')
label1.pack(**pack_dict)

value1 = tk.StringVar(value=5.0)
# will be string even using a tk.DoubleVar()
#value1 = tk.DoubleVar()
# tk.Spinbox() from 0 to 30
# wrap=True  one 'to' is reached restarts with 'from_'
# defaults are increment=1  width=20 (characters)
# Python already has keyword 'from' so 'from_' is used
spin_box1 = tk.Spinbox(
    root,
    from_=0,
    to=30,
    increment=0.1,
    font=myfont,
    bg='lime',
    width=10,
    textvariable=value1,
    wrap=True,
    command=value_changed)
# you can use the given pack dictionary
spin_box1.pack(**pack_dict)

label2 =tk.Label(root, text='Years to pay:')
label2.pack(**pack_dict)

value2 = tk.StringVar(value=15)
# tk.Spinbox() from 0 to 50
spin_box2 = tk.Spinbox(
    root,
    from_=0,
    to=50,
    increment=1,
    font=myfont,
    bg='yellow',
    width=10,
    textvariable=value2,
    wrap=True,
    command=value_changed)
# you can use the given pack dictionary
spin_box2.pack(**pack_dict)

label3 =tk.Label(root, text='Principle Loan $:')
label3.pack(**pack_dict)

value3 = tk.StringVar(value=200000)
# tk.Spinbox() from 0 to 800 thousand
spin_box3 = tk.Spinbox(
    root,
    from_=0,
    to=800000,
    increment=1000,
    font=myfont,
    bg='aqua',
    width=10,
    textvariable=value3,
    wrap=True,
    command=value_changed)
# you can use the given pack dictionary
spin_box3.pack(**pack_dict)

cour12b = ('courier', 12, 'bold')
scrollbar = tk.Scrollbar(root)
# width and height depend on character size
text1 = tk.Text(root, 
                width=40, 
                height=30, 
                bg='wheat',
                font=cour12b,
                yscrollcommand=scrollbar.set)
scrollbar.config(command=text1.yview)
scrollbar.pack(side='right', fill='y')
text1.pack(**pack_dict)

# show initial starting text
value_changed()

root.mainloop()
