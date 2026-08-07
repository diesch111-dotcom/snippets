#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' moon_phases.py

determine the moon phase at a given date
(mildly off on moon's light intensity)
checked with http://aa.usno.navy.mil/data/docs/RS_OneDay.html

Chinese New Year falls on the second new moon after the winter solstice
celebrated to sweep away the bad luck and attracting the good luck!

Some Chinese New Year dates (lasts a total moon cycle):
Gregorian   Date    Animal  Day of the week 
2023        22 Jan  Rabbit  Sunday
2024        10 Feb  Dragon  Saturday
2025        29 Jan  Snake   Wednesday
2026        17 Feb  Horse   Tuesday
2027        6 Feb   Goat    Saturday
2028        26 Jan  Monkey  Wednesday
2029        13 Feb  Rooster Tuesday
2030        3 Feb   Dog     Sunday
2031        23 Jan  Pig     Thursday
2032        11 Feb  Rat     Wednesday
2033        31 Jan  Ox      Monday
2034        19 Feb  Tiger   Sunday

tested with Spyder IDE on LinuxMint  vegaseat 15jun2026
'''

import calendar
 
def get_weekday2(year, month, day):
    '''
    given the date as year, month, day
    return the day of the week
    Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday
    using python module calendar
    '''
    weekday_list = [day for day in calendar.day_name]
    weekday = weekday_list[calendar.weekday(year, month, day)]
    return weekday

def moon_phase(month, day, year):
    ages = [18, 0, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7]
    offsets = [-1, 1, 0, 1, 2, 3, 4, 5, 7, 7, 9, 9]
    description = ["new (totally dark)",
      "waxing crescent (increasing to full)",
      "in its first quarter (increasing to full)",
      "waxing gibbous (increasing to full)",
      "full (full light)",
      "waning gibbous (decreasing from full)",
      "in its last quarter (decreasing from full)",
      "waning crescent (decreasing from full)"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if day == 31:
        day = 1
    days_into_phase = ((ages[(year + 1) % 19] +
                        ((day + offsets[month-1]) % 30) +
                        (year < 1900)) % 30)
    index = int((days_into_phase + 2) * 16/59.0)
    #print(index)  # test
    if index > 7:
        index = 7
    status = description[index]
    # light should be 100% 15 days into phase
    light = int(2 * days_into_phase * 100/29)
    if light > 100:
        light = abs(light - 200);
    date = "%d%s%d" % (day, months[month-1], year)
    return date, status, light


# put in a date you want ...
# Chinese New Year falls on the second new moon after the winter solstice
month = 6
day = 15
year = 2026  # use yyyy format

date, status, light = moon_phase(month, day, year)
week_day = get_weekday2(year, month, day)
print(f"moon phase on {week_day} {date} is {status}")
date, status, light = moon_phase(month=1, day=17, year=2026)
print(f"moon phase on {date} is {status}")


''' result...
moon phase on Monday 15Jun2026 is new (totally dark)
moon phase on 17Jan2026 is waning crescent (decreasing from full)
'''
