#!/usr/bin/env python3
# -*- coding: utf-8 -*
''' time_epoch.py

A closer look at time module use of epoch
and the effect of GMT timezone and your local timezone


time.struct_time object has the following attributes:
tm_year: the year, for example, 2021
tm_mon: the month, in the range [1, 12]
tm_mday: the day of the month, in the range [1, 31]
tm_hour: the hour, in the range [0, 23]
tm_min: the minute, in the range [0, 59]
tm_sec: the second, in the range [0, 61]
tm_wday: the weekday, in the range [0, 6], Monday is 0
tm_yday: the day of the year, in the range [1, 366]
tm_isdst: 0, 1 or -1, depending on daylight saving time

if you have seconds since epoch ...
time.localtime(secs)  Returns a tuple representing time :
  (year aaaa, month(1-12), day(1-31), hour(0-23), minute(0-59),
  second(0-59), weekday(0-6, 0 is monday), Julian day(1-366),
  daylight flag(-1,0 or 1))  considers local time zone

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

import time

print("module time has this epoch beginning date:")
epoch = '01.01.1970 00:00:00'
print(epoch)
print("epoch seconds will be local relative to GMT:")
epoch_seconds =time.mktime(time.strptime(epoch, "%m.%d.%Y %H:%M:%S"))
print(epoch_seconds)

'''
module time has this epoch beginning date:
01.01.1970 00:00:00
epoch seconds will be local relative to GMT:
28800.0
'''

print('='*30)

print("get current GMT seconds:")
gmt_seconds = time.mktime(time.gmtime())
print(gmt_seconds)
print("get current local seconds (depends on your timezone):")
local_seconds = time.mktime(time.localtime())
print(local_seconds)

'''
get current GMT seconds:
1786267203.0
get current local seconds (depends on your timezone):
1786238403.0
'''

print('='*30)

print("get the difference (GMT - local):")
gmt_local_difference = gmt_seconds - local_seconds
print(gmt_local_difference)

'''
get the difference (GMT - local):
28800.0
'''

print('='*30)

print("true GMT based epoch seconds:")
print(epoch_seconds - gmt_local_difference) 

'''some results based on Pacific Timezone ...
true GMT based epoch seconds:
0.0
'''

print('='*30)

# create a time.struct_time object
# a named tuple
t = time.struct_time((2021, 9, 13, 10, 30, 0, 0, 256, 0))
print(t)

''' possible result...

time.struct_time(tm_year=2021, tm_mon=9, tm_mday=13, tm_hour=10, 
                 tm_min=30, tm_sec=0, tm_wday=0, tm_yday=256, tm_isdst=0)
'''

print('='*30)

# convert it to seconds since the epoch 
# mm.dd.yyyy = 01.01.1970 and hh:mm:ss = 00:00:00
s = time.mktime(t)

print(f'{s:,} seconds since epoch')

''' possible result...
1,631,557,800.0 seconds since epoch
'''

print('='*30)

# notice tm_hour and tm_isdst difference
print(time.localtime(s))

''' possible result...
time.struct_time(tm_year=2021, tm_mon=9, tm_mday=13, tm_hour=11, 
                 tm_min=30, tm_sec=0, tm_wday=0, tm_yday=256, tm_isdst=1)
'''

print('='*30)

# when seconds since epoch is omitted, then current local time is used
print(time.localtime())

'''  possible result...
time.struct_time(tm_year=2026, tm_mon=8, tm_mday=8, tm_hour=18, 
                 tm_min=23, tm_sec=9, tm_wday=5, tm_yday=220, tm_isdst=1)
'''
