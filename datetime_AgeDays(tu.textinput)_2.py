#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' datetime_AgeDays(tu.textinput)_2.py

Use module datetime to show age in days
modified to work with SublimeText IDE ...
does not like python input(), so use turtle.textinput()

Some interesting birthdays:
Joe Biden born 20nov1942
Donald Trump born 14jun1946
Xi Jinping born 15jun1953 (studied chemical engineering)
Vladimir Putin born 07oct1952

tested with SublimeText IDE on LinuxMint    vegaseat  15jun2026
'''

import datetime as dt

'''
prompt = "Enter your birthday (format = mm/dd/yyyy): "
try:
    # Python2
    bd = raw_input(prompt)
except NameError:
    # Python3
    bd = input(prompt)
'''

import turtle as tu

tu.Screen().setup(15, 15)
# string input
bd = tu.textinput("Birthday", "Enter a birthday (format = mm/dd/yyyy):")

# split the bd string into month, day, year
month, day, year = bd.split("/")

# convert to format datetime.date(year, month, day))
birthday = dt.date(int(year), int(month), int(day))

# get todays date
today = dt.date.today()

# calculate age since birth
age = (today - birthday)

print(f"Today is {today}")

print(f"Born on {bd}, you are {age.days} days old!")

# extra stuff
XiJinping_bd =  dt.date(1953, 6, 15)
JoeBiden_bd = dt.date(1942, 11, 20)
DonaldTrump_bd = dt.date(1946, 6, 14)

age_xj = (today - XiJinping_bd)
print(f'Xi Jinping born {XiJinping_bd} is {age_xj.days} days old')

age_jb = (today - JoeBiden_bd)
print(f'Joe Biden born {JoeBiden_bd} is {age_jb.days} days old')

age_dt = (today - DonaldTrump_bd)
print(f'Donald Trump born {DonaldTrump_bd} is {age_dt.days} days old')

''' possible result...
Today is 2026-08-02
Born on 06/15/1941, you are 31094 days old!
Xi Jinping born 1953-06-15 is 26711 days old
Joe Biden born 1942-11-20 is 30571 days old
Donald Trump born 1946-06-14 is 29269 days old
'''
