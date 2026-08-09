#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' time_current_h_m_s.py

Use Python module time to get the current
hour, minute and second values

IDLE usually comes with Python install, to gain access...
might have to install the IDLE IDE, in the Linux terminal use:
sudo apt update
sudo apt install idle3
...once installed this way, it shows up under 'Programming' as IDLE

tested with IDLE IDE on LinuxMint  vegaseat 19jul2026
'''
import time

# take a slice of the current time tuple
# values you want are in index 3, 4, 5  so unpack
hr, min, sec = time.localtime()[3:6]

# test
sf = "Current time values are {} hours {} minutes and {} seconds"
print(sf.format(hr, min, sec))

''' possible result ...
Current time values are 18 hours 27 minutes and 6 seconds
'''

# another option ...
now = time.localtime()
#print(now)  # test
sf = "Current time values are {} hours {} minutes and {} seconds"
print(sf.format(now.tm_hour, now.tm_min, now.tm_sec))
