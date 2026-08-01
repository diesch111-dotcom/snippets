#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' data_10_most_populated_countries_2025.py

raw data from Google Gemini...

global human population stands at ~8.3 billion people 
1 billion = 1e9 = 1_000_000_000

tested using the SublimeText IDE on Linux  vegaseat  15jun2026
'''

import pprint

print("10 Most Populated Countries 2025:")
# '~' separated 
data = '''\
1India~1.46 – 1.47 Billion~18.0%
2China~1.41 Billion~17.5%
3United States~348 – 349 Million~4.3%
4Indonesia~286 – 287 Million~3.5%
5Pakistan~259 – 261 Million~3.2%
6Nigeria~242 – 243 Million~3.0%
7Brazil~212 – 222 Million~2.6%
8Bangladesh~175 – 177 Million~2.2%
9Russia~140 – 144 Million~1.8%
10Ethiopia~135 – 139 Million~1.7%'''

country_list = []
for ix, line in enumerate(data.split('\n'), start=1):
	rcountry, population, percent = line.split('~')
	country = "".join([c for c in rcountry if c.isalpha()])
	#print(country)
	country_list.append([ix, country, population, percent])

pprint.pprint(country_list)

'''
10 Most Populated Countries 2025:
[[1, 'India', '1.46 – 1.47 Billion', '18.0%'],
 [2, 'China', '1.41 Billion', '17.5%'],
 [3, 'UnitedStates', '348 – 349 Million', '4.3%'],
 [4, 'Indonesia', '286 – 287 Million', '3.5%'],
 [5, 'Pakistan', '259 – 261 Million', '3.2%'],
 [6, 'Nigeria', '242 – 243 Million', '3.0%'],
 [7, 'Brazil', '212 – 222 Million', '2.6%'],
 [8, 'Bangladesh', '175 – 177 Million', '2.2%'],
 [9, 'Russia', '140 – 144 Million', '1.8%'],
 [10, 'Ethiopia', '135 – 139 Million', '1.7%']]
'''
