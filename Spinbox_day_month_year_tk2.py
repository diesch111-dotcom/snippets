#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Spinbox_day_month_year_tk2.py

A neat way to click through dates!
Create a date with day, month, year tkinter tk.Spinbox()
uses the tasteful tk.LabelFrame() for each tk.Spinbox()
Then display the weekday and formatted date
day=15 month=6 year=1941 should show: Sunday 15 Jun 1941

Module 'datetime' checks for impossible dates
like maximum days of February in leapyears

docs
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/shipman/spinbox.html
https://tkdocs.com/shipman/label.html
https://tkdocs.com/shipman/grid.html
https://tkdocs.com/shipman/labelframe.html


using the Spyder IDE on Linux  dns(vegaseat) 8jul2026
"""

from datetime import date
import calendar
import tkinter as tk


def click_spinbox():
    """
    get day, month, year values and process the data
    """
    day = int(sb_day.get())
    month = int(sb_month.get())
    year = int(sb_year.get())
    try:
        date_obj = date(year, month, day)
        # get a list of day names (starts with Monday by default)
        week_day = list(calendar.day_name)
        date_weekday = week_day[date_obj.weekday()]
        date_date = date_obj.strftime('%d %b %Y')
        # date is 'weekday dd month_str yyyy' format
        ds = f"{date_weekday} {date_date}"
    except ValueError:
        ds = "Impossible date, check days!" 
    label['text'] = ds
    # testing...
    print(ds)


root = tk.Tk()
root['bg'] = 'darkgreen'
root.title("enter day month year via spinboxes")
# set Upper Left Corner (x, y) position of root
root.geometry("+%d+%d" % (100, 120))

v_day = tk.IntVar()
# preset day to 15
v_day.set(15)
frame_day = tk.LabelFrame(root, text=" select a day ", bd=3)
#frame_day.pack(side='left', padx=5, pady=5)
frame_day.grid(row=0, column=0, padx=5, pady=5)
# goes from 1 to 31 in steps of 1 (default)
sb_day = tk.Spinbox(frame_day, from_=1, to=31, textvariable=v_day, 
    command=click_spinbox, width=10)

v_month = tk.IntVar()
# preset month to 6
v_month.set(6)
frame_month = tk.LabelFrame(root, text=" select a month ", bd=3)
#frame_month.pack(side='left', padx=5, pady=5)
frame_month.grid(row=0, column=1, padx=5, pady=5)
# goes from 1 to 12 in steps of 1 (default)
sb_month = tk.Spinbox(frame_month, from_=1, to=12, textvariable=v_month, 
    command=click_spinbox, width=10)

v_year = tk.IntVar()
# preset to year 2000
v_year.set(1941)
frame_year = tk.LabelFrame(root, text=" select a year ", bd=3)
#frame_year.pack(side='left', padx=5, pady=5)
frame_year.grid(row=0, column=2, padx=5, pady=5)
# goes from 1930 to 2050 in steps of 1 (default)
sb_year = tk.Spinbox(frame_year, from_=1930, to=2050, textvariable=v_year, 
    command=click_spinbox, width=10)


label = tk.Label(root, bg='yellow', width=25, font=['Arial', 16])

# here the grid layout manger is more intuitive
# column and row count starts at zero
label.grid(row=1, column=0, columnspan=3, pady=10)
sb_day.grid(row=0, column=0, padx=10, pady=5)
sb_month.grid(row=0, column=1, padx=10, pady=5)
sb_year.grid(row=0, column=1, padx=10, pady=5)

# initial action
click_spinbox()

root.mainloop()
