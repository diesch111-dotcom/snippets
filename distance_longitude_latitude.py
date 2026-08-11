#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' distance_longitude_latitude.py

Given the longitudes and latitudes of two cities, calculate the distance

Uses the Haversine Formula recommended for calculating short
distances by NASA's Jet Propulsion Laboratory.  For longer
distances this formula tends to overestimate trans-polar distances and
underestimate trans-equatorial distances.

Note:
latitude N(+90) to S(-90), equator = 0
longitude W(-180) to E(+180), prime meridian (Greenwich UK) = 0

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    '''
    calculate the great circle distance between two points
    on the Earth (coordinates specified in decimal degrees)
    '''
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))

    # 6367 km (3961 miles) is the radius of the Earth
    km = 6367 * c
    miles = 3961 * c
    return km, miles


# Detroit, Michigan  48235
city1 = "Detroit"
lat1  = 42.4261
lon1 = -83.1951

# Chicago, Illinois  60290
city2 = "Chicago"
lat2  = 41.9613
lon2 = -87.8849

km, miles = haversine(lon1, lat1, lon2, lat2)

sf = "The distance between {} and {} is {:0.1f} miles (air)"
print(sf.format(city1, city2, miles))

'''
The distance between Detroit and Chicago is 242.3 miles (air)
'''
