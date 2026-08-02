#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' day_of_week.py

get the day of the week given a date string mm/dd/yyyy or yyyy/mm/dd
using python module time

July 4, 1776 was on a Thursday
3/14/1879 was on a Friday (Albert Einstein's birthday aka. pi-day)

can also use:
weekday_list2 = list(calendar.day_name)
for a list of weekdays

tested with SublimeText IDE on LinuxMint    vegaseat  15jun2026
'''

import time

def get_day_of_week(date_str):
    '''
    day of week of a given month/day/year date string format mm/dd/yyyy
    returns index Monday = 0, Tuesday = 1, ...
    '''
    t1 = time.strptime(date_str, "%m/%d/%Y")
    # year can not go below 01/01/1970 at 0 UT (midnight Greenwich, England)
    # which is the start of epoch for module time
    t2 = time.mktime(t1)
    return time.localtime(t2)[6]

# much simpler ...

def get_day_of_week2(date_str):
    '''
    day of week of a given month/day/year date string format mm/dd/yyyy
    returns index Monday = 0, Tuesday = 1, ...
    does not use time.mktime() and its start of epoch limit 1/1/1970
    '''
    return time.strptime(date_str, "%m/%d/%Y")[6]

weekday_list = [
'Monday', 'Tuesday', 'Wednesday', 'Thursday',
'Friday', 'Saturday', 'Sunday'
]

# test ...
# date string month/day/year needs format mm/dd/yyyy
# note: leading zero is not needed, can be 5/16/1976
date_str = "05/16/1976"
print("{} was a {}".format(date_str, weekday_list[get_day_of_week(date_str)]))

print('-'*22)

date_str = "7/4/1776"
print("{} was a {}".format(date_str, 
    weekday_list[get_day_of_week2(date_str)]))

print('-'*22)

date_str = "3/14/1879"
print("{} was a {}".format(date_str, 
    weekday_list[get_day_of_week2(date_str)]))

'''
05/16/1976 was a Sunday
----------------------
7/4/1776 was a Thursday
----------------------
3/14/1879 was a Friday
'''

print('-'*22)

# changed to year/month/day format
# %Y  Year with century as a decimal number
# %m  Month as a decimal number 01 to 12
# %d  Day of the month as a decimal number 01 to 31


def get_day_of_week3(date_str):
    '''
    day of week of a given a date string of format yyyy/mm/dd
    returns index Monday = 0, Tuesday = 1, ...
    '''
    return time.strptime(date_str, "%Y/%m/%d")[6]


# date string month/day/year needs format mm/dd/yyyy
# note: leading zero is not needed, can be "1941/6/15"
date_str = "1941/06/15"
print("{} was a {}".format(date_str, 
    weekday_list[get_day_of_week3(date_str)]))

'''
1941/06/15 was a Sunday
'''
