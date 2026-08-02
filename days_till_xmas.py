#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' days_till_xmas.py

Calculate shopping days till xmas

tested with SublimeText IDE on LinuxMint    vegaseat  15jun2026
'''

import datetime as dt

now = dt.date.today()
# takes care of the 6 days after xmas (ffao)
year = now.year + (dt.date(now.year, 12, 25) < now)
xmas = dt.date(year, 12, 25)
till_xmas = xmas - now

print(f"There are {till_xmas.days} shopping days till xmas this year!")
